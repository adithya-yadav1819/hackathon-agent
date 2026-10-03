from app.llm.client import LLMClient

class VerifierAgent:
    def __init__(self):
        self.llm = LLMClient()

    def verify_findings(self, raw_evidence: str, analyst_findings: str):
        """
        Acts as an independent fact-checker. It reviews the analyst's findings
        and cross-references them strictly against the raw evidence.
        """
        system_prompt = (
            "You are a strict digital forensics auditor and verifier. "
            "Your job is to review the Analyst's findings and cross-check them "
            "against the raw evidence. If a claim is made without direct support "
            "from the evidence, flag it as 'UNVERIFIED' or 'FABRICATED'."
        )

        messages = [
            {"role": "system", "content": system_prompt},
            {
                "role": "user", 
                "content": f"RAW EVIDENCE:\n{raw_evidence}\n\nANALYST FINDINGS TO VERIFY:\n{analyst_findings}"
            }
        ]

        response = self.llm.chat(messages)
        return {
            "status": "VERIFIED",
            "audit_report": response
        }