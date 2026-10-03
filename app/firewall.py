class EvidenceFirewall:
    def sanitize_and_check(self, raw_evidence: str) -> dict:
        """
        Inspects incoming raw evidence containers to ensure they are safe 
        and properly encapsulated before passing them to the AI agents.
        """
        # Simple check for malicious instruction injections or breakout attempts
        dangerous_keywords = ["ignore previous instructions", "system override", "drop database"]
        
        for keyword in dangerous_keywords:
            if keyword in raw_evidence.lower():
                return {
                    "is_safe": False,
                    "reason": f"Security violation detected: Forbidden keyword '{keyword}' found in evidence.",
                    "wrapped_data": ""
                }

        # Wrap the evidence in a strict data container boundary
        wrapped_data = (
            "--- BEGIN EVIDENCE CONTAINER (UNTRUSTED) ---\n"
            f"{raw_evidence}\n"
            "--- END EVIDENCE CONTAINER ---"
        )

        return {
            "is_safe": True,
            "reason": "Evidence passed security screening.",
            "wrapped_data": wrapped_data
        }