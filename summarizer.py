from dotenv import load_dotenv
import os
import re

load_dotenv()


def _local_summary(text, sentence_limit=5):
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    sentences = [s.strip() for s in sentences if s.strip()]
    if not sentences:
        return ""
    return " ".join(sentences[:sentence_limit])


def summarize_text(text):
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        return _local_summary(text)

    try:
        from groq import Groq
    except ImportError:
        return _local_summary(text)

    client = Groq(api_key=api_key)

    try:
        response = client.chat.completions.create(
            model_name="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": f"Summarize the following research paper in 150-200 words:\n\n{text[:4000]}"
                }
            ]
        )
        return response.choices[0].message.content
    except Exception:
        return _local_summary(text)