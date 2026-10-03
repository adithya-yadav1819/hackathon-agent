from app.llm.client import LLMClient

class CrossExaminationAgent:
    def __init__(self):
        self.llm = LLMClient()

    def challenge_findings(self, analyst_findings: str):
        """
        Acts as a defense attorney / skeptic. It challenges the AI's findings
        to find alternative, benign explanations for suspicious behavior.
        """
        system_prompt = (
            "You are a critical defense counsel and red-team skeptic in a DFIR investigation. "
            "Your goal is to poke holes in the analyst's conclusions. Look for "
            "alternative benign explanations (e.g., legitimate IT administration tasks, "
            "scheduled maintenance, false positives) for the reported indicators."
        )

        messages = [
            {"role": "system", "content": system_prompt},
            {
                "role": "user", 
                "content": f"Challenge these findings and offer alternative benign explanations if possible:\n{analyst_findings}"
            }
        ]

        response = self.llm.chat(messages)
        return {
            "status": "CHALLENGED",
            "counter_analysis": response
        }