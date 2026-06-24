from flask import Flask, render_template, request
import google.generativeai as genai

app = Flask(__name__)

# Gemini API Key
genai.configure(api_key="YOUR_API_KEY_HERE")

model = genai.GenerativeModel("gemini-2.5-flash")

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        topic = request.form.get("topic")

        prompt = f"""
        Topic: {topic}

        Generate the following:

        1. Short Summary
        2. Detailed Notes
        3. Key Points (Bullet List)
        4. 20 Quick Practice Questions

        Format properly with headings.
        """

        try:
            response = model.generate_content(prompt)
            result = response.text
        except Exception as e:
            result = f"Error: {str(e)}"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)