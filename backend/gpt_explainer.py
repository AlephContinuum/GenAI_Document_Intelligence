
import openai
from config.secrets import OPENAI_API_KEY
openai.api_key=OPENAI_API_KEY

def explain_text(text):
    completion=openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":f"Explain the following document:\n{text[:2000]}"}]
    )
    return completion.choices[0].message["content"]
