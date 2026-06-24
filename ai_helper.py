import google.generativeai as genai

API_KEY = "YOUR_API_KEY"

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")


def generate_notes(topic):
    prompt = f"""
    Generate short study notes for:
    {topic}

    Include:
    - Summary
    - Key Points
    """

    response = model.generate_content(prompt)
    return response.text


def generate_quiz(topic):
    prompt = f"""
    Generate 5 MCQs on {topic}
    """

    response = model.generate_content(prompt)

    questions = response.text.split("\n")
    return questions
