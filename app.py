import os
import json
import io
from flask import Flask, request, jsonify, render_template
from openai import OpenAI
import PyPDF2
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY", "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"),
    base_url="https://openrouter.ai/api/v1"
)
MODEL = "openrouter/auto"

# ─────────────────────────────────────────────
# AI HELPERS
# ─────────────────────────────────────────────

def call_ai(system, user):
    try:
        res = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": system},
                {"role": "user",   "content": user}
            ],
            temperature=0.5,
            max_tokens=2000
        )
        return res.choices[0].message.content.strip()
    except Exception as e:
        return f"ERROR: {e}"


def generate_summary(text):
    system = """You are a study assistant. Summarize the provided content in detail.
Return a JSON object with this exact structure:
{
  "title": "Topic title in 5 words or less",
  "overview": "4-5 sentence overview covering the main themes and key conclusions",
  "key_points": ["full sentence point 1", "full sentence point 2", "full sentence point 3", "full sentence point 4", "full sentence point 5", "full sentence point 6", "full sentence point 7", "full sentence point 8"]
}
Make each key point a full informative sentence with specific details, not just a short phrase.
Return ONLY the JSON. No markdown, no extra text."""
    raw = call_ai(system, text[:8000])
    try:
        return json.loads(raw.replace("```json","").replace("```","").strip())
    except:
        return {"title": "Summary", "overview": raw, "key_points": []}


def generate_flashcards(text):
    system = """You are a study assistant. Create 6 flashcards from the provided content.
Return a JSON array with this exact structure:
[
  {"front": "Question or term", "back": "Answer or definition"},
  ...
]
Return ONLY the JSON array. No markdown, no extra text."""
    raw = call_ai(system, text[:4000])
    try:
        return json.loads(raw.replace("```json","").replace("```","").strip())
    except:
        return []


def generate_quiz(text):
    system = """You are a study assistant. Create 10 multiple choice questions from the provided content.
Return a JSON array with this exact structure:
[
  {
    "question": "The question text",
    "options": ["A) option", "B) option", "C) option", "D) option"],
    "answer": "A) correct option",
    "explanation": "Brief explanation why"
  }
]
Make sure all 10 questions are included. Cover different parts of the content.
Return ONLY the JSON array. No markdown, no extra text."""
    raw = call_ai(system, text[:8000])
    try:
        return json.loads(raw.replace("```json","").replace("```","").strip())
    except:
        return []


def generate_mindmap(text):
    system = """You are a study assistant. Create a mind map outline from the provided content.
Return a JSON object with this exact structure:
{
  "center": "Main Topic",
  "branches": [
    {
      "label": "Branch 1",
      "children": ["subtopic 1", "subtopic 2", "subtopic 3"]
    },
    {
      "label": "Branch 2",
      "children": ["subtopic 1", "subtopic 2"]
    }
  ]
}
Create 4-5 branches with 2-4 children each.
Return ONLY the JSON. No markdown, no extra text."""
    raw = call_ai(system, text[:4000])
    try:
        return json.loads(raw.replace("```json","").replace("```","").strip())
    except:
        return {"center": "Main Topic", "branches": []}


def extract_pdf_text(file_bytes):
    try:
        reader = PyPDF2.PdfReader(io.BytesIO(file_bytes))
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text.strip()
    except Exception as e:
        return f"ERROR: {e}"


# ─────────────────────────────────────────────
# ROUTES
# ─────────────────────────────────────────────

def get_text_from_request():
    data = request.get_json()
    if "pdf" in data:
        import base64
        pdf_bytes = base64.b64decode(data["pdf"])
        return extract_pdf_text(pdf_bytes)
    return data.get("text", "")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/summary", methods=["POST"])
def api_summary():
    text = get_text_from_request()
    return jsonify(generate_summary(text))


@app.route("/api/flashcards", methods=["POST"])
def api_flashcards():
    text = get_text_from_request()
    return jsonify(generate_flashcards(text))


@app.route("/api/quiz", methods=["POST"])
def api_quiz():
    text = get_text_from_request()
    return jsonify(generate_quiz(text))


@app.route("/api/mindmap", methods=["POST"])
def api_mindmap():
    text = get_text_from_request()
    return jsonify(generate_mindmap(text))


# ─────────────────────────────────────────────
# ENTRY POINT
# ─────────────────────────────────────────────
if __name__ == "__main__":
    print("\n🎓 AI Study Assistant")
    print("   Running at: http://127.0.0.1:5000\n")
    app.run(debug=True)
