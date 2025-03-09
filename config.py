from dotenv import load_dotenv
import os


load_dotenv()


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY","")

if not OPENAI_API_KEY:
    raise ValueError("No OpenAI API Key provided. Set an API key in the OPENAI_API_KEY in the .env file.")

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

RESULTS_DIR = os.path.join(BASE_DIR, "results")

os.makedirs(os.path.dirname(RESULTS_DIR), exist_ok=True)