import os
import openai
from dotenv import load_dotenv
from openai import OpenAI

class LLMWrapper:
    def __init__(self, model="gpt-3.5-turbo"):
        load_dotenv(dotenv_path="apikey1.env")
        api_key = os.getenv("openai_apikey")

        if not api_key:
            raise ValueError("API key not found in apikey1.env")

        self.model = model
        self.client = OpenAI(api_key=api_key)

    def ask(self, prompt, temperature=0.7, max_tokens=500):
        try:
            print(f"Sending prompt: {prompt}")
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=temperature,
                max_tokens=max_tokens
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"Error: {e}"

if __name__ == "__main__":
    llm = LLMWrapper()
    response = llm.ask("What is the capital of France?")
    print("LLM Response:", response)
