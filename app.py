import os
import whisper
from flask import Flask, request, render_template, redirect
from dotenv import load_dotenv
from google import genai

# ---- Setup ----
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load Whisper model once when server starts (faster than reloading every request)
print("Loading Whisper model...")
whisper_model = whisper.load_model("tiny")
print("Whisper model loaded!")


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", transcript=None, summary=None)


@app.route("/upload", methods=["POST"])
def upload():
    if "audio_file" not in request.files:
        return redirect("/")

    audio_file = request.files["audio_file"]
    if audio_file.filename == "":
        return redirect("/")

    # Save uploaded file
    filepath = os.path.join(UPLOAD_FOLDER, audio_file.filename)
    audio_file.save(filepath)

    # Transcribe
    result = whisper_model.transcribe(filepath)
    transcript = result["text"]

    # Summarize
    prompt = f"""Summarize this meeting transcript into key decisions and action items.

Transcript:
{transcript}
"""
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )
    summary = response.text

    return render_template("index.html", transcript=transcript, summary=summary)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
