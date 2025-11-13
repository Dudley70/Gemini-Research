"""
External Traceability Validator for Gemini Research Prompt v4.8.1

Validates that executive_summary[0] (the direct answer) is properly supported
by high or medium confidence findings with traceable sources.

Operates as external orchestrator component - research prompt prepares
traceability_data, this validator computes aggregate confidence and policy compliance.

Usage:
    from external_traceability_validator import validate_traceability
    
    gemini_output = {...}  # JSON from Gemini Research Prompt
    traceability_results = validate_traceability(gemini_output)
    
    if traceability_results['status'] == 'VERIFIED':
        # Answer is well-supported
        print("Answer claim verified with H/M confidence support")
    else:
        # Answer is speculative or unsupported
        print(f"Warning: {traceability_results['notes']}")
"""

from typing import Dict, List, Any
from datetime import datetime


def validate_traceability(gemini_output: Dict[str, Any]) -> Dict[str, Any]:
    """
    Validates that executive_summary[0] is supported by H/M confidence findings.
    
    Args:
        gemini_output: JSON output from Gemini Research Prompt v4.8.1
    
    Returns:
        Dictionary containing:
        - traceability: Validated traceability data with aggregate confidence
        - status: VERIFIED | SPECULATIVE | ERROR
        - notes: Explanation of validation result
    """
    
    # Extract data
    try:
        executive_summary = gemini_output['executive_summary']
        findings = gemini_output['key_findings']
        sources = gemini_output['sources']
        traceability_data = gemini_output['meta']['traceability_data']
    except KeyError as e:
        return _create_error_result(f"Missing required field: {e}")
    
    answer_claim = traceability_data.get('answer_claim', '')
    supporting_finding_ids = traceability_data.get('supporting_finding_ids', [])
    
    # Validate answer claim matches executive_summary[0]
    if not answer_claim:
        return _create_error_result("No answer_claim in traceability_data")
    
    if not executive_summary or len(executive_summary) == 0:
        return _create_error_result("No executive_summary in output")
    
    # Executive summary item 1 should be the answer
    expected_answer = executive_summary[0]
    
    # Extract just the text (without source citations)
    # Format: "1. Direct answer to question [source_id(s)]"
    expected_text = expected_answer.split('[')[0].strip()
    if expected_text.startswith('1.'):
        expected_text = expected_text[2:].strip()
    
    # Validate supporting findings exist
    if not supporting_finding_ids:
        return {
            "traceability": {
                "answer_claim": answer_claim,
                "expected_answer": expected_text,
                "support": {
                    "finding_ids": [],
                    "source_ids": [],
                    "aggregate_confidence": "None",
                    "meets_policy": False
                }
            },
            "status": "SPECULATIVE",
            "notes": "No supporting findings identified for answer claim",
            "validation_metadata": _get_metadata(gemini_output)
        }
    
    # Get actual findings
    findings_by_id = {f['id']: f for f in findings}
    supporting_findings = []
    missing_ids = []
    
    for finding_id in supporting_finding_ids:
        if finding_id in findings_by_id:
            supporting_findings.append(findings_by_id[finding_id])
        else:
            missing_ids.append(finding_id)
    
    if missing_ids:
        return _create_error_result(
            f"Referenced finding IDs not found in findings: {missing_ids}"
        )
    
    # Extract confidences and source IDs
    confidences = [f['confidence'] for f in supporting_findings]
    all_source_ids = []
    for f in supporting_findings:
        all_source_ids.extend(f.get('source_ids', []))
    
    # Deduplicate source IDs
    unique_source_ids = list(set(all_source_ids))
    
    # Compute aggregate confidence
    aggregate_confidence = _compute_aggregate_confidence(confidences)
    
    # Check policy (requires H or M)
    meets_policy = aggregate_confidence in ['H', 'M']
    
    # Determine status
    if meets_policy:
        status = "VERIFIED"
        notes = f"Answer supported by {len(supporting_findings)} finding(s) with {aggregate_confidence} confidence"
    else:
        status = "SPECULATIVE"
        notes = f"Answer only supported by {aggregate_confidence} confidence finding(s) - needs H or M confidence"
    
    # Validate source IDs exist
    missing_sources = [sid for sid in unique_source_ids if sid not in sources]
    if missing_sources:
        status = "ERROR"
        notes = f"Referenced source IDs not found: {missing_sources}"
    
    # Build detailed support breakdown
    support_breakdown = []
    for finding in supporting_findings:
        support_breakdown.append({
            "finding_id": finding['id'],
            "finding_text": finding['text'][:100] + "..." if len(finding['text']) > 100 else finding['text'],
            "confidence": finding['confidence'],
            "source_ids": finding['source_ids'],
            "source_count": len(finding['source_ids'])
        })
    
    return {
        "traceability": {
            "answer_claim": answer_claim,
            "expected_answer": expected_text,
            "claim_match": _calculate_similarity(answer_claim, expected_text),
            "support": {
                "finding_ids": supporting_finding_ids,
                "source_ids": unique_source_ids,
                "aggregate_confidence": aggregate_confidence,
                "meets_policy": meets_policy
            },
            "support_breakdown": support_breakdown
        },
        "status": status,
        "notes": notes,
        "validation_metadata": _get_metadata(gemini_output)
    }


def _compute_aggregate_confidence(confidences: List[str]) -> str:
    """
    Computes aggregate confidence from list of individual confidences.
    
    Rules:
    - If any H → aggregate is H (highest confidence available)
    - If no H but at least one M → aggregate is M
    - If only L → aggregate is L
    - If empty → aggregate is None
    """
    if not confidences:
        return "None"
    
    if 'H' in confidences:
        return 'H'
    elif 'M' in confidences:
        return 'M'
    else:
        return 'L'


def _calculate_similarity(claim: str, expected: str) -> str:
    """
    Simple heuristic to check if claim and expected answer are similar.
    
    Returns: "match" | "partial" | "mismatch"
    """
    claim_lower = claim.lower().strip()
    expected_lower = expected.lower().strip()
    
    # Exact match
    if claim_lower == expected_lower:
        return "exact_match"
    
    # Check if one contains the other
    if claim_lower in expected_lower or expected_lower in claim_lower:
        return "partial_match"
    
    # Check word overlap
    claim_words = set(claim_lower.split())
    expected_words = set(expected_lower.split())
    
    # Remove common stop words
    stop_words = {'a', 'an', 'the', 'is', 'are', 'was', 'were', 'to', 'from', 'in', 'on', 'at', 'for'}
    claim_words -= stop_words
    expected_words -= stop_words
    
    if not claim_words or not expected_words:
        return "insufficient_data"
    
    overlap = claim_words & expected_words
    overlap_ratio = len(overlap) / max(len(claim_words), len(expected_words))
    
    if overlap_ratio >= 0.7:
        return "high_overlap"
    elif overlap_ratio >= 0.4:
        return "moderate_overlap"
    else:
        return "low_overlap"


def _get_metadata(gemini_output: Dict[str, Any]) -> Dict[str, str]:
    """Extracts validation metadata from Gemini output."""
    run_metadata = gemini_output.get('meta', {}).get('run_metadata', {})
    
    return {
        "validator_version": "1.0.0",
        "prompt_version": run_metadata.get('prompt_version', 'unknown'),
        "validated_at": datetime.now().isoformat()
    }


def _create_error_result(error_message: str) -> Dict[str, Any]:
    """Creates error result structure when validation cannot proceed."""
    return {
        "traceability": {
            "answer_claim": "",
            "expected_answer": "",
            "claim_match": "error",
            "support": {
                "finding_ids": [],
                "source_ids": [],
                "aggregate_confidence": "None",
                "meets_policy": False
            },
            "support_breakdown": []
        },
        "status": "ERROR",
        "notes": f"Validation error: {error_message}",
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
        "executive_summary": [
            "1. Desktop and Code use separate memory systems requiring manual coordination [1, 3]",
            "2. Desktop uses automatic chat synthesis [1, 2]",
            # ... other items
        ],
        "key_findings": [
            {
                "id": 1,
                "text": "Desktop Memory uses automatic chat synthesis with 24-hour update cycles",
                "source_ids": ["1", "2"],
                "confidence": "H"
            },
            {
                "id": 2,
                "text": "Desktop Memory cannot overcome token limits through synthesis",
                "source_ids": ["1"],
                "confidence": "M"
            },
            {
                "id": 3,
                "text": "Code Memory uses CLAUDE.md file hierarchy with Git integration",
                "source_ids": ["3", "4"],
                "confidence": "H"
            },
            {
                "id": 4,
                "text": "No native integration exists between Desktop and Code memory systems",
                "source_ids": ["5", "6"],
                "confidence": "H"
            }
        ],
        "sources": {
            "1": {"publisher": "Anthropic", "title": "Desktop Memory Guide"},
            "2": {"publisher": "Anthropic Docs", "title": "Memory Synthesis"},
            "3": {"publisher": "Claude Code Docs", "title": "CLAUDE.md Specification"},
            "4": {"publisher": "GitHub", "title": "Claude Code Examples"},
            "5": {"publisher": "Anthropic", "title": "Platform Comparison"},
            "6": {"publisher": "ClaudeWorkflow", "title": "Integration Research"}
        },
        "meta": {
            "traceability_data": {
                "answer_claim": "Desktop and Code maintain separate memory systems with no native integration",
                "supporting_finding_ids": [1, 3, 4]
            },
            "run_metadata": {
                "prompt_version": "4.8.1"
            }
        }
    }
    
    # Validate traceability
    results = validate_traceability(example_output)
    
    print("Traceability Validation Results:")
    print(f"Status: {results['status']}")
    print(f"Notes: {results['notes']}")
    print(f"\nSupport Details:")
    print(f"  Answer Claim: {results['traceability']['answer_claim']}")
    print(f"  Aggregate Confidence: {results['traceability']['support']['aggregate_confidence']}")
    print(f"  Meets Policy: {results['traceability']['support']['meets_policy']}")
    print(f"  Finding IDs: {results['traceability']['support']['finding_ids']}")
    print(f"  Source IDs: {results['traceability']['support']['source_ids']}")
    
    print(f"\nSupport Breakdown:")
    for item in results['traceability']['support_breakdown']:
        print(f"  Finding {item['finding_id']} ({item['confidence']}): {item['finding_text']}")
