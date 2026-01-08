from dotenv import load_dotenv
import os

# Load variables from .env into environment
load_dotenv()

# Read Groq API key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if GROQ_API_KEY is None:
    raise ValueError("GROQ_API_KEY not found. Check your .env file.")
