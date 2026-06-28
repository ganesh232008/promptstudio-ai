import google.generativeai as genai
from backend.config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def collect_requirements(conversation):

    response = model.generate_content(
        f"""
You are the Requirement Agent of PromptForge AI.

Conversation:

{conversation}

------------------------------------

Your job is to determine whether enough information
has been collected to create the final prompt.

If information is missing:

Reply ONLY with concise follow-up questions.

If enough information has been collected:

Reply ONLY with

ENOUGH_INFORMATION

Do NOT explain anything.
Do NOT generate the final prompt.
"""
    )

    return response.text.strip()