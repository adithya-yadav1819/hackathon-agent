import os
from google import genai

class LLMClient:
    def __init__(self):
        # Looks for GEMINI_API_KEY in your environment
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise RuntimeError(
                "GEMINI_API_KEY is not set. Set it in your environment before running."
            )
        self.client = genai.Client(api_key=api_key)
        # Using Gemini 2.5 Flash / 1.5 Flash as the free default model
        self.model = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

    def chat(self, messages: list[dict[str, str]]) -> str:
        # Convert standard OpenAI message format into a single prompt for Gemini
        prompt_parts = []
        for msg in messages:
            role = msg.get("role", "user")
            content = msg.get("content", "")
            prompt_parts.append(f"{role.upper()}: {content}")
        
        full_prompt = "\n".join(prompt_parts)

        response = self.client.models.generate_content(
            model=self.model,
            contents=full_prompt,
        )
        return response.text