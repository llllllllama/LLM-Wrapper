# llm_wrapper.py

import openai
from dotenv import load_dotenv
import os

class LLMWrapper:
    def __init__(self, model="gpt-3.5-turbo"):
        load_dotenv(dotenv_path="apikey1.env")  # ✅ Load your .env file here
        self.api_key = os.getenv("openai_apikey")  # ✅ Get the key from environment
        raise ValueError("API key not found. Set 'openai_apikey' in your .env file.")

        self.model = model
        openai.api_key = self.api_key  # ✅ Set OpenAI to use this key

    def ask(self, prompt, temperature=0.7, max_tokens=500):
        try:
            print(f"Sending prompt: {prompt}")
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=temperature,
                max_tokens=max_tokens
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"Error: {e}"
