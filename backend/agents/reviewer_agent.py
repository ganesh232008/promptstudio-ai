import google.generativeai as genai
from backend.config import GEMINI_API_KEY

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def review_prompt(prompt):
    """
    Reviewer Agent

    Reviews the generated prompt for quality.
    It should improve the prompt only if necessary.
    """

    response = model.generate_content(
        f"""
You are the Reviewer Agent of PromptForge AI.

Your responsibility is ONLY to review the prompt.

Prompt:

{prompt}

------------------------------------------

Review Checklist:

✓ Clear
✓ Professional
✓ Complete
✓ Easy to understand
✓ Grammatically correct
✓ Well structured
✓ No ambiguity
✓ Suitable for AI models
✓ No unnecessary repetition

Rules:

1. If the prompt is already excellent,
   return it unchanged.

2. If improvements are needed,
   improve ONLY the prompt.

3. Do NOT explain your changes.

4. Do NOT add comments.

5. Return ONLY the reviewed prompt.
"""
    )

    return response.text.strip()