import google.generativeai as genai
from backend.config import GEMINI_API_KEY

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def optimize_prompt(prompt):
    """
    Optimizer Agent

    Makes the prompt stronger while preserving
    the original meaning.
    """

    response = model.generate_content(
        f"""
You are the Optimizer Agent of PromptForge AI.

Your job is to optimize the prompt.

Prompt:

{prompt}

----------------------------------------

Optimize it by making it:

✓ More detailed
✓ More structured
✓ Easier for AI to understand
✓ More professional
✓ More precise
✓ Better organized

Rules:

1. Keep the original meaning.

2. Never remove important information.

3. Never ask new questions.

4. Return ONLY the optimized prompt.
"""
    )

    return response.text.strip()