from flask import Flask, render_template, request
from google import genai

# Initialize Gemini client
client = genai.Client(api_key="AIzaSyBwN40eFlpxD_d79WE1xbjwjD30sGrSCY4")

app = Flask(__name__)

def build_prompt(target_language, current_level, time_commitment):
    return f"""
    Generate a language-learning plan for
    Target Language: {target_language}
    Current Level: {current_level}
    Time Commitment: {time_commitment}

   Create a detailed learning plan using clean, minimal HTML.
Give instructions at last about completion and other references."""

@app.route("/")
def home():
    return render_template("input.html")

@app.route("/generate", methods=["POST"])
def generate():
    target_language = request.form.get("target_language", "")
    current_level = request.form.get("current_level", "")
    time_commitment = request.form.get("time_commitment", "")

    prompt = build_prompt(target_language, current_level, time_commitment)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    final_html = response.text

    return render_template("result.html", response=final_html)

if __name__ == "__main__":
    app.run(debug=True)
