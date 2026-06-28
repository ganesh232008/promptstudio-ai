import google.generativeai as genai
ffrom config import GEMINI_API_KEY

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_prompt(conversation):
    """
    Prompt Generator Agent

    This agent assumes the Requirement Agent has already collected
    enough information from the user.

    It generates ONE final professional prompt.
    """

    response = model.generate_content(
        f"""
You are the Prompt Generator Agent of PromptForge AI.

Your ONLY responsibility is to create a HIGH-QUALITY prompt.

The Requirement Agent has already finished collecting all required information.

Conversation History:

{conversation}

====================================================

Your task:

1. Read the complete conversation carefully.

2. Extract every important requirement.

3. Create ONE final professional AI prompt.

The prompt should be suitable for:

• ChatGPT
• Google Gemini
• Claude
• Microsoft Copilot
• Any modern LLM

Requirements:

✔ Well structured
✔ Professional
✔ Detailed
✔ Easy to understand
✔ Optimized for the best AI response

DO NOT:

❌ Ask more questions
❌ Explain anything
❌ Answer the user's request
❌ Add unnecessary text

Return ONLY the final optimized prompt.
"""
    )

    return response.text.strip()