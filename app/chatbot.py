import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def ask_ai(question):
    prompt = f"""
    You are an expert Agriculture AI Assistant.

    Rules:
    1. Answer ONLY agriculture, farming, crops, fertilizers, irrigation, pesticides, diseases, weather and crop yield questions.
    2. If the question is outside agriculture, reply:
    "I can only answer agriculture-related questions."
    3. Keep answers short (maximum 5-6 lines).
    4. Give practical farmer-friendly advice.
    5. Mention fertilizer or pesticide only when appropriate.

    Question:
    {question}
    """

    try:
        response = client.models.generate_content(
            model="models/gemini-2.5-flash",
            contents=prompt
        )
        return response.text

    except Exception:
        return "⚠ AI service is temporarily unavailable. Please try again later."