import google.generativeai as genai
from config import GEMINI_API_KEY

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def format_prompt(prompt):
    """
    Formatter Agent

    Formats the final prompt into a clean,
    professional and readable structure.
    """

    response = model.generate_content(
        f"""
You are the Formatter Agent of PromptForge AI.

Your ONLY responsibility is formatting.

Prompt:

{prompt}

-----------------------------------------

Format the prompt professionally.

Requirements:

✓ Add a clear title if appropriate
✓ Use headings
✓ Use bullet points where needed
✓ Keep paragraphs readable
✓ Improve spacing
✓ Keep ALL information
✓ Do NOT change the meaning

Rules:

1. Do NOT ask questions.

2. Do NOT explain anything.

3. Do NOT add comments.

4. Return ONLY the formatted prompt.
"""
    )

    return response.text.strip()