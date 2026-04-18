# 🎓 AI Study Assistant
🚀 **[Live Demo](https://ai-study-assistant-g4ar.onrender.com)**

> **Note on Performance:** This application is hosted on Render's free tier. If the site has been inactive, it may take **30-50 seconds** to "wake up" (cold start) while the server provisions resources. Once active, it will respond instantly.

An AI-powered web application that transforms complex lecture notes and university PDFs into structured study materials instantly. This tool utilizes Large Language Models to automate the creation of summaries, interactive flashcards, and quizzes.

## ✨ Key Features

Upload a PDF or paste your notes to generate:

| Feature | Description |
|:---|:---|
| 📋 **Summary** | Generates a topic title, concise overview, and 5 key bullet points. |
| 🃏 **Flashcards** | Creates 6 interactive flip cards with questions on the front and answers on the back. |
| ❓ **Quiz** | Build a 5-question multiple-choice quiz with instant feedback and scoring. |
| 🗺️ **Mind Map** | Renders a visual canvas showing the main topic and its supporting branches. |

## 🛠️ Tech Stack

- **Python (Flask)** — Backend web server and REST API logic
- **OpenRouter API** — LLM integration for intelligent content generation
- **PyPDF2** — Robust text extraction from uploaded PDF documents
- **HTML5/CSS3/JS** — Responsive, modern frontend interface
- **Canvas API** — Dynamic rendering of the interactive mind map

## 📂 Project Structure

```text
ai_study_assistant/
├── app.py            # Main application logic & AI prompt engineering
├── requirements.txt  # Python dependencies (Flask, OpenAI, PyPDF2, etc.)
├── templates/        # UI directory
│   └── index.html    # Single-page dashboard interface
└── README.md         # Project documentation