# 🎙️ Meeting Summarizer

A web app that transcribes meeting audio and generates AI-powered summaries with key decisions and action items.

## Features
- Upload an audio file through a simple web interface
- Automatic speech-to-text transcription using OpenAI Whisper
- AI-generated summary highlighting key decisions and action items using Google Gemini

## Tech Stack
- **Backend:** Python, Flask
- **Speech-to-Text:** OpenAI Whisper (running locally)
- **LLM:** Google Gemini API
- **Frontend:** HTML (Flask templates)

## How It Works
1. User uploads an audio file via the web interface
2. Whisper transcribes the audio into text
3. The transcript is sent to Gemini with a prompt asking it to extract key decisions and action items
4. The transcript and summary are displayed on the page

## Setup Instructions

### Prerequisites
- Python 3.11
- ffmpeg installed (`brew install ffmpeg` on Mac)
- A free Gemini API key from [Google AI Studio](https://aistudio.google.com/apikey)

### Installation
1. Clone this repository

2. Create and activate a virtual environment

3. Install dependencies

4. Create a `.env` file in the project root and add your Gemini API key:

5. Run the app

6. Open your browser and go to `http://127.0.0.1:5000`

## Testing
A sample audio file (`sample.flac`) is included in this repo for quick testing — it's an ~11 second clip of a JFK speech excerpt.

## Project Structure
