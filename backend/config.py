import os
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

# Get the Gemini API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")