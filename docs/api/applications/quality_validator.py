"""
External Quality Validator for Gemini Research Prompt v4.8.1

Scores research output using the QUALITY FRAMEWORK defined in the prompt.
Operates as external orchestrator component - research prompt produces data,
this validator computes quality scores.

Usage:
    from external_quality_validator import validate_research_quality
    
    gemini_output = {...}  # JSON from Gemini Research Prompt
    quality_results = validate_research_quality(
        gemini_output,
        total_dimensions=10  # Based on research objective
    )
    
    if quality_results['threshold'] == 'Production':
        # Approve for use in Decision Log
        print("Research approved for production use")
    elif quality_results['threshold'] == 'Marginal':
        # Flag for human review or enhancement
        print("Research needs review or enhancement")
    else:
        # Redesign approach
        print("Research has fundamental gaps - redesign needed")
"""

from typing import Dict, List, Optional, Any
from datetime import datetime, timedelta


def validate_research_quality(
    gemini_output: Dict[str, Any],
    total_dimensions: int,
    freshness_applicable: bool = True
) -> Dict[str, Any]:
    """
    Validates and scores research output using Quality Framework formulas.
    
    Args:
        gemini_output: JSON output from Gemini Research Prompt v4.8.1
        total_dimensions: Total number of dimensions the research should address
                         (derived from objective or manual specification)
        freshness_applicable: Whether freshness scoring applies to this topic
                             (False for stable topics like Python syntax)
    
    Returns:
        Dictionary containing:
        - quality_assessment: Scores and justifications for each criterion
        - threshold: Production | Marginal | Insufficient
        - recommended_action: What to do with this research
        - claudeworkflow_action: Specific action for ClaudeWorkflow
    """
    
    # Extract data from Gemini output
    findings = gemini_output.get('key_findings', [])
    sources = gemini_output.get('sources', {})
    
    # Validate input structure
    if not findings:
        return _create_error_result("No findings in research output")
    
    if not sources:
        return _create_error_result("No sources in research output")
    
    # Compute Coverage Score
    coverage_score, coverage_justification = _compute_coverage(
        findings, total_dimensions
    )
    
    # Compute Evidence Score
    evidence_score, evidence_justification = _compute_evidence(findings)
    
    # Compute Freshness Score (if applicable)
    if freshness_applicable:
        freshness_score, freshness_justification = _compute_freshness(sources)
    else:
        freshness_score = None
        freshness_justification = "N/A - Stable topic, freshness not applicable"
    
    # Compute Contradictions Score
    disagreements = gemini_output.get('meta', {}).get('disagreements', [])
    contradictions_score, contradictions_justification = _compute_contradictions(
        disagreements
    )
    
    # Compute Average (excluding None values)
    scores = [coverage_score, evidence_score, contradictions_score]
    if freshness_score is not None:
        scores.append(freshness_score)
    
    average_score = sum(scores) / len(scores)
    
    # Determine Threshold and Actions
    threshold_data = _determine_threshold(average_score)
    
    return {
        "quality_assessment": {
            "coverage": {
                "score": round(coverage_score, 1),
                "justification": coverage_justification
            },
            "evidence": {
                "score": round(evidence_score, 1),
                "justification": evidence_justification
            },
            "freshness": {
                "score": round(freshness_score, 1) if freshness_score is not None else None,
                "justification": freshness_justification
            },
            "contradictions": {
                "score": round(contradictions_score, 1),
                "justification": contradictions_justification
            },
            "average": round(average_score, 1)
        },
        "threshold": threshold_data['threshold'],
        "recommended_action": threshold_data['action'],
        "claudeworkflow_action": threshold_data['claudeworkflow_action'],
        "validation_metadata": {
            "validator_version": "1.0.0",
            "prompt_version": gemini_output.get('meta', {}).get('run_metadata', {}).get('prompt_version', 'unknown'),
            "validated_at": datetime.now().isoformat(),
            "total_dimensions_used": total_dimensions,
            "freshness_applicable": freshness_applicable
        }
    }


def _compute_coverage(findings: List[Dict], total_dimensions: int) -> tuple:
    """
    Coverage = (dimensions_addressed / total_dimensions) × 10
    
    Dimensions are unique themes/topics addressed in findings.
    Simple heuristic: count unique first 2-3 words of finding text as dimension indicator.
    """
    if total_dimensions <= 0:
        return 0.0, "Error: total_dimensions must be > 0"
    
    # Extract dimension indicators from findings
    # Heuristic: first 2-3 words typically indicate the dimension/topic
    dimensions_found = set()
    
    for finding in findings:
        text = finding.get('text', '')
        # Extract first 3 words as dimension indicator
        words = text.split()[:3]
        dimension_key = ' '.join(words).lower()
        dimensions_found.add(dimension_key)
    
    dimensions_addressed = len(dimensions_found)
    score = (dimensions_addressed / total_dimensions) * 10
    
    # Cap at 10
    score = min(score, 10.0)
    
    justification = f"{dimensions_addressed}/{total_dimensions} dimensions addressed"
    if score >= 9.0:
        justification += " (comprehensive coverage)"
    elif score >= 7.0:
        justification += " (good coverage with minor gaps)"
    else:
        justification += " (significant gaps in coverage)"
    
    return score, justification


def _compute_evidence(findings: List[Dict]) -> tuple:
    """
    Evidence = (findings_with_H_or_M_confidence / total_findings) × 10
    """
    if not findings:
        return 0.0, "No findings to assess"
    
    hm_findings = [f for f in findings if f.get('confidence') in ['H', 'M']]
    total_findings = len(findings)
    
    score = (len(hm_findings) / total_findings) * 10
    
    h_count = len([f for f in findings if f.get('confidence') == 'H'])
    m_count = len([f for f in findings if f.get('confidence') == 'M'])
    l_count = len([f for f in findings if f.get('confidence') == 'L'])
    
    justification = f"{len(hm_findings)}/{total_findings} findings with H/M confidence "
    justification += f"(H:{h_count}, M:{m_count}, L:{l_count})"
    
    if score >= 8.0:
        justification += " - strong primary source support"
    elif score >= 6.0:
        justification += " - adequate evidence base"
    else:
        justification += " - insufficient primary sources"
    
    return score, justification


def _compute_freshness(sources: Dict[str, Any]) -> tuple:
    """
    Freshness = (sources ≤ 180 days / total_sources) × 10
    """
    if not sources:
        return 0.0, "No sources to assess"
    
    cutoff_date = datetime.now() - timedelta(days=180)
    recent_count = 0
    total_count = len(sources)
    date_parse_errors = 0
    
    for source_id, source_data in sources.items():
        date_str = source_data.get('date', '')
        if not date_str:
            continue
        
        try:
            # Parse YYYY-MM-DD format
            source_date = datetime.strptime(date_str, '%Y-%m-%d')
            if source_date >= cutoff_date:
                recent_count += 1
        except ValueError:
            date_parse_errors += 1
            continue
    
    if total_count == 0:
        return 0.0, "No sources with valid dates"
    
    score = (recent_count / total_count) * 10
    
    justification = f"{recent_count}/{total_count} sources ≤ 180 days"
    if date_parse_errors > 0:
        justification += f" ({date_parse_errors} date parse errors)"
    
    if score >= 8.0:
        justification += " - predominantly recent sources"
    elif score >= 5.0:
        justification += " - mixed recency"
    else:
        justification += " - mostly dated sources"
    
    return score, justification


def _compute_contradictions(disagreements: List[Dict]) -> tuple:
    """
    Contradictions = 10 - (unresolved_conflicts × 2)
    
    Unresolved = disagreements with final_stance='uncertain'
    """
    if not disagreements:
        return 10.0, "No contradictions found (0 conflicts)"
    
    unresolved = [d for d in disagreements if d.get('final_stance') == 'uncertain']
    unresolved_count = len(unresolved)
    
    score = 10 - (unresolved_count * 2)
    score = max(score, 0.0)  # Floor at 0
    
    total_disagreements = len(disagreements)
    resolved_count = total_disagreements - unresolved_count
    
    justification = f"{unresolved_count} unresolved conflicts "
    justification += f"({resolved_count}/{total_disagreements} resolved)"
    
    if score >= 8.0:
        justification += " - contradictions well-handled"
    elif score >= 6.0:
        justification += " - some unresolved conflicts remain"
    else:
        justification += " - significant unresolved contradictions"
    
    return score, justification


def _determine_threshold(average_score: float) -> Dict[str, str]:
    """
    Determines threshold category and associated actions based on average score.
    """
    if average_score >= 8.0:
        return {
            'threshold': 'Production',
            'action': 'Approve for use in templates/documentation.',
            'claudeworkflow_action': 'Add to Decision Log, use in Phase 1 template design'
        }
    elif average_score >= 7.0:
        return {
            'threshold': 'Marginal',
            'action': 'Flag for human review or run enhancement pass.',
            'claudeworkflow_action': 'Sufficient for exploration, not for architectural decisions'
        }
    else:
        return {
            'threshold': 'Insufficient',
            'action': 'Redesign research approach or provide more context.',
            'claudeworkflow_action': 'Do not use - missing critical information for decision-making'
        }


def _create_error_result(error_message: str) -> Dict[str, Any]:
    """Creates error result structure when validation cannot proceed."""
    return {
        "quality_assessment": {
            "coverage": {"score": 0, "justification": error_message},
            "evidence": {"score": 0, "justification": error_message},
            "freshness": {"score": None, "justification": "N/A"},
            "contradictions": {"score": 0, "justification": error_message},
            "average": 0.0
        },
        "threshold": "Insufficient",
        "recommended_action": f"Fix validation error: {error_message}",
        "claudeworkflow_action": "Cannot use - validation failed",
        "validation_metadata": {
            "validator_version": "1.0.0",
            "validated_at": datetime.now().isoformat(),
            "error": error_message
        }
    }


# Example usage
if __name__ == "__main__":
    # Example Gemini output (simplified)
    example_output = {
        "key_findings": [
            {"id": 1, "text": "Desktop Memory uses automatic chat synthesis", "source_ids": ["1", "2"], "confidence": "H"},
            {"id": 2, "text": "Desktop Memory updates on 24-hour cycles", "source_ids": ["1"], "confidence": "M"},
            {"id": 3, "text": "Code Memory uses CLAUDE.md file system", "source_ids": ["3", "4"], "confidence": "H"},
            {"id": 4, "text": "Code Memory integrates with Git", "source_ids": ["3"], "confidence": "M"},
            {"id": 5, "text": "Integration requires manual handoff protocols", "source_ids": ["5"], "confidence": "M"}
        ],
        "sources": {
            "1": {"date": "2025-01-15", "publisher": "Anthropic"},
            "2": {"date": "2025-01-10", "publisher": "Anthropic Docs"},
            "3": {"date": "2025-01-20", "publisher": "Claude Code Docs"},
            "4": {"date": "2024-12-15", "publisher": "GitHub"},
            "5": {"date": "2025-01-18", "publisher": "ClaudeWorkflow"}
        },
        "meta": {
            "disagreements": [
                {"claim": "Memory sharing possible", "final_stance": "against", "confidence": "H"}
            ],
            "run_metadata": {"prompt_version": "4.8.1"}
        }
    }
    
    # Validate quality
    results = validate_research_quality(
        example_output,
        total_dimensions=3,  # Desktop, Code, Integration
        freshness_applicable=True
    )
    
    print("Quality Assessment Results:")
    print(f"Average Score: {results['quality_assessment']['average']}/10")
    print(f"Threshold: {results['threshold']}")
    print(f"Action: {results['recommended_action']}")
    print(f"\nDetailed Scores:")
    for criterion, data in results['quality_assessment'].items():
        if criterion != 'average':
            print(f"  {criterion.capitalize()}: {data['score']}/10 - {data['justification']}")
