import os
from pathlib import Path

from dotenv import load_dotenv
from google import genai

# -----------------------------
# Load Environment Variables
# -----------------------------

BASE_DIR = Path(__file__).resolve().parents[2]

load_dotenv(BASE_DIR / ".env", override=True)

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found")

client = genai.Client(api_key=api_key)


# ==========================================================
# GENERAL PROGRAMMING MENTOR
# ==========================================================

def ask_gemini(prompt: str):

    system_prompt = f"""
You are CodeMentor AI.

You are an expert software engineer and programming mentor.

Always answer in a beginner-friendly way.

Whenever appropriate include:

1. Simple explanation
2. Real-world analogy
3. Step-by-step explanation
4. Code examples
5. Time Complexity
6. Space Complexity
7. Common interview questions
8. Common mistakes
9. Best practices

User Question:

{prompt}
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=system_prompt,
        )

        return response.text

    except Exception as e:

        error = str(e)

        if "429" in error:
            return (
                "⚠️ API quota exceeded.\n\n"
                "Please try again later."
            )

        if "503" in error:
            return (
                "🚧 Gemini is currently experiencing high demand.\n\n"
                "Please wait a few seconds and try again."
            )

        return f"Unexpected Error:\n\n{error}"


# ==========================================================
# GENERATE CODE
# ==========================================================

def generate_code(language: str, problem: str):

    prompt = f"""
You are an expert software engineer.

Generate clean, production-quality {language} code.

Problem:

{problem}

Include:

1. Solution
2. Explanation
3. Time Complexity
4. Space Complexity
5. Best Practices
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        return response.text

    except Exception as e:
        return str(e)


# ==========================================================
# EXPLAIN CODE
# ==========================================================

def explain_code(language: str, code: str):

    prompt = f"""
Explain the following {language} code.

Code:

{code}

Explain:

1. Line by line
2. Beginner friendly
3. Time Complexity
4. Space Complexity
5. Improvements
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        return response.text

    except Exception as e:
        return str(e)


# ==========================================================
# DEBUG CODE
# ==========================================================

def debug_code(language: str, code: str):

    prompt = f"""
You are an expert debugger.

Language:

{language}

Code:

{code}

Find:

1. Bugs
2. Logic errors
3. Syntax errors
4. Fix them
5. Explain each fix
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        return response.text

    except Exception as e:
        return str(e)


# ==========================================================
# REVIEW CODE
# ==========================================================

def review_code(language: str, code: str):

    prompt = f"""
Review this {language} code.

Code:

{code}

Review:

1. Readability
2. Performance
3. Best Practices
4. Security
5. Suggestions
6. Overall Rating (/10)
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        return response.text

    except Exception as e:
        return str(e)