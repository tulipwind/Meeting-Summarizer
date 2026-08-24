import os
import sys
import whisper
from dotenv import load_dotenv
from google import genai

# ---- Step A: Load our API key ----
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

# ---- Step B: Get the audio file name from user ----
if len(sys.argv) < 2:
    print("Usage: python pipeline.py <audio_file>")
    sys.exit(1)

audio_file = sys.argv[1]

# ---- Step C: Transcribe audio using Whisper ----
print(f"Transcribing {audio_file}... (this may take a moment)")
whisper_model = whisper.load_model("tiny")
result = whisper_model.transcribe(audio_file)
transcript = result["text"]

print("\n--- TRANSCRIPT ---")
print(transcript)

# ---- Step D: Send transcript to Gemini for summarization ----
prompt = f"""Summarize this meeting transcript into key decisions and action items.

Transcript:
{transcript}
"""

print("\nGenerating summary...")
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=prompt
)
summary = response.text

print("\n--- SUMMARY ---")
print(summary)

# ---- Step E: Save both to files ----
base_name = os.path.splitext(os.path.basename(audio_file))[0]

with open(f"{base_name}_transcript.txt", "w") as f:
    f.write(transcript)

with open(f"{base_name}_summary.txt", "w") as f:
    f.write(summary)

print(f"\n✅ Saved: {base_name}_transcript.txt and {base_name}_summary.txt")
