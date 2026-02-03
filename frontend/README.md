# 📘 Fixed Content Q&A Agent (Without Vector DB)

An AI-powered Question & Answer system where users upload fixed documents and ask questions strictly from those documents.

This project demonstrates:

- FastAPI backend
- React frontend
- LangChain agent usage
- Structured prompt engineering
- Direct document context retrieval
- End-to-end AI + API + UI workflow

---

## 🚀 Project Overview

Users can:

1. Upload  documents
2. Backend reads and stores document content
3. Ask questions from the UI
4. AI answers ONLY from the uploaded document content



---

## 🏗️ Architecture

```
React Frontend
      ↓
FastAPI Backend
      ↓
LangChain Agent
      ↓
LLM with Document Context
```

---

## 🖥️ Tech Stack

### Frontend
- React.js
- Axios

### Backend
- FastAPI
- LangChain
- OpenAI / LLM
- PyPDF / TextLoader

---

##  Prompt Strategy (Core Logic)

System Prompt used by the agent:

> You are a Q&A assistant.  
> You must answer ONLY from the provided document content.  
> If the answer is not present, say:  
> **"The answer is not available in the provided documents."**

This ensures:

- No hallucinations
- No external knowledge
- Fully controlled responses

---


## 📤 API Endpoints

### Upload Documents

```
POST /upload
```

Reads document content and stores it in memory for questioning.

---

### Ask Question

```
POST /ask
Body: { "question": "Your question" }
```

Response:

```json
{
  "answer": "Answer from documents"
}
```

---

## 🔄 Agent Workflow

1. User uploads documents
2. Backend extracts text from documents
3. Text is stored in memory
4. User asks a question
5. Document text + question sent to LLM
6. Prompt forces LLM to answer only from text
7. Answer returned to UI

---

## 🎯 Key Features

- Multi-document support
- Controlled AI responses
- Clean UI
- Clear separation of frontend and backend
- Prompt-driven document Q&A system

---

## 🛡️ Safety Rule

If the answer is not found:

> "The answer is not available in the provided documents."

---

## 🖼️ UI Features

- Document upload section
- Question input box
- Loading state while fetching answer
- Answer display card

---

## 🏁 Outcome of This Project

This project demonstrates:

- LangChain agent usage
- Prompt engineering
- LLM document grounding
- Full stack AI application development

---


