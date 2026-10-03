from app.llm.client import LLMClient
from app.firewall import EvidenceFirewall

class AnalystAgent:
    def __init__(self):
        self.llm = LLMClient()
        self.firewall = EvidenceFirewall()

    def analyze_logs(self, raw_log_text: str):
        """
        Takes raw log evidence, runs it through the firewall, 
        and uses the LLM to investigate malicious indicators.
        """
        # Step 1: Run evidence through the firewall for security
        safety_check = self.firewall.sanitize_and_check(raw_log_text)
        
        if not safety_check["is_safe"]:
            return {
                "status": "SECURITY_ALERT",
                "message": safety_check["reason"],
                "findings": []
            }

        # Step 2: Prompt the AI detective to analyze the safe data
        system_prompt = (
            "You are a senior digital forensics expert. Analyze the provided "
            "untrusted evidence container for suspicious PowerShell commands, "
            "phishing attachments, or malware persistence. "
            "Every finding MUST include exact evidence references."
        )

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Investigate this evidence:\n{safety_check['wrapped_data']}"}
        ]

        # Step 3: Call the LLM client we built earlier
        response = self.llm.chat(messages)
        return {
            "status": "SUCCESS",
            "analysis": response
        }