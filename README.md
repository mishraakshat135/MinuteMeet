# 🎙️ MinuteMeet – AI Meeting Intelligence Platform

MinuteMeet is an end-to-end AI meeting assistant that transforms meeting recordings into actionable insights. It automatically transcribes audio, generates concise summaries, extracts action items, identifies key decisions, highlights open questions, and enables conversational Q&A over meeting transcripts using Retrieval-Augmented Generation (RAG).

Designed using modern AI engineering practices, MinuteMeet combines Speech AI, LLMs, semantic search, and vector databases into a unified workflow.

---

# 🚀 Features

- 🎥 Process local audio/video files or YouTube recordings
- 🎙️ Automatic Speech-to-Text transcription
- 🌐 English and Hinglish transcription support
- 📝 AI-generated meeting title
- 📋 Professional meeting summaries
- ✅ Action item extraction
- 🔑 Key decision extraction
- ❓ Open question detection
- 📚 RAG-powered meeting chatbot
- 🔍 Semantic search using vector embeddings
- ⚡ Modular AI pipeline

---

# 🧠 AI Pipeline

```
Meeting Recording / YouTube Video
               │
               ▼
Audio Extraction
               │
               ▼
Whisper / Sarvam AI
               │
               ▼
Meeting Transcript
               │
      ┌────────┼────────┐
      ▼        ▼        ▼
 Summary   Action Items  Decisions
      │        │         │
      └────────┼─────────┘
               ▼
      Chroma Vector Store
               │
               ▼
       RAG Question Answering
```

---

# 🛠 Tech Stack

## Programming Language

- Python

## Speech AI

- OpenAI Whisper
- Sarvam AI

## Generative AI

- LangChain
- Mistral AI

## Retrieval-Augmented Generation

- ChromaDB
- HuggingFace Embeddings
- RecursiveCharacterTextSplitter

## Audio Processing

- yt-dlp
- pydub
- FFmpeg

## Frontend

- Streamlit

---

# 📚 AI Concepts Demonstrated

- Speech-to-Text (STT)
- Natural Language Processing
- Retrieval-Augmented Generation (RAG)
- Vector Databases
- Semantic Search
- Prompt Engineering
- Information Extraction
- Meeting Intelligence
- Large Language Models (LLMs)

---

# 💡 Workflow

1. Upload a local recording or provide a YouTube URL.
2. Audio is extracted and converted to WAV.
3. Whisper (English) or Sarvam AI (Hinglish) generates the transcript.
4. The transcript is analyzed to generate:
   - Meeting title
   - Summary
   - Action items
   - Key decisions
   - Open questions
5. A Chroma vector database is built from the transcript.
6. Users can ask natural language questions, answered using RAG over the meeting content.

---

# 📖 Skills Demonstrated

- AI Engineering
- Speech AI
- Whisper
- LangChain
- Mistral AI
- ChromaDB
- RAG
- Vector Embeddings
- Semantic Search
- Prompt Engineering
- Information Extraction
- Python

---

# 🎯 Future Improvements

- Speaker diarization
- PDF/DOCX meeting minutes export
- Timestamped transcripts
- Multi-meeting workspace
- Authentication
- React + FastAPI frontend
- Calendar integration
- Email meeting summaries
- Team collaboration
- Multi-language support

---

# 👨‍💻 Author

**Akshat Mishra**

B.Tech in Data Science & Artificial Intelligence  
Thapar Institute of Engineering & Technology

---

⭐ If you found this project useful, consider giving it a star!