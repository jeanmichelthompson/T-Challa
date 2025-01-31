# openai_client.py
import os
import openai
import dotenv

dotenv.load_dotenv()
openai.api_key = os.getenv("OPENAI_KEY")

# Easy to modify system instructions:
SYSTEM_PROMPT = """You are a helpful and encouraging coach. 
Offer advice tailored to the user, with an uplifting and positive style.
Keep your responses concise yet thorough. 
"""

def get_coach_reply(user_prompt: str) -> str:
    # Build a simple conversation with a system and user message.
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_prompt},
    ]

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=messages,
            temperature=0.5
        )
        # Return just the text of the assistant's message
        return response.choices[0].message["content"]
    except Exception as e:
        print(f"OpenAI API error: {e}")
        return "Sorry, I'm having trouble coaching right now."
