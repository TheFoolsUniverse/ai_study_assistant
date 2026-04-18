# 🎓 AI Study Assistant

An AI-powered web app that transforms lecture notes or PDFs into study materials instantly.

## What It Does

Upload a PDF or paste your notes → get:

| Feature | Description |
|---------|-------------|
| 📋 Summary | Title, overview, and key bullet points |
| 🃏 Flashcards | 6 interactive flip cards (tap to reveal answer) |
| ❓ Quiz | 5 MCQs with instant feedback and score |
| 🗺️ Mind Map | Visual canvas showing topic structure |

## Tech Stack

- **Python** — Core language
- **Flask** — Web server & REST API
- **OpenRouter API** — LLM for content generation
- **PyPDF2** — PDF text extraction
- **HTML/CSS/JS** — Frontend (single file, no frameworks)
- **Canvas API** — Mind map rendering

## Project Structure

```
ai_study_assistant/
├── app.py            ← main file (run this)
├── requirements.txt
├── .env              ← your API key
└── README.md