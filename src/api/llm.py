import os
from dotenv import load_dotenv
import cohere

load_dotenv()

COHERE_API_KEY = os.getenv("COHERE_API_KEY")

co = cohere.Client(COHERE_API_KEY)

def query_llm(prompt):
    try:
        response = co.generate(
            model='command-light',
            prompt=prompt,
            max_tokens=150,
            temperature=0.7,
        )
        return response.generations[0].text
    except Exception as e:
        return f"Error communicating with LLM: {str(e)}"
