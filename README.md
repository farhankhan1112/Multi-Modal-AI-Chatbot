# Multi-Modal AI Chatbot using GenAI

A Streamlit-based **multi-modal AI chatbot** powered by **Google Gemini (Generative AI)** that supports:

- 💬 Text-based conversations  
- 🖼️ Image + text analysis  
- 📄 PDF document question answering  

This project demonstrates how a single AI application can intelligently handle **multiple input modalities** using modern GenAI models.

---

## 🚀 Features

- **💬 Text Chat**
  - General-purpose conversational AI
  - Handles open-ended questions and explanations
  - Maintains session-based chat history

- **🖼️ Image + Text Analysis**
  - Upload images (JPG, PNG, JPEG)
  - Ask contextual questions about the image

- **📄 PDF Document Chat**
  - Upload PDF documents (e.g., resumes, reports)
  - Ask questions grounded strictly in document content
  - Extracts and analyzes text from PDFs to reduce hallucinations

- **Session-based Chat History**
  - Maintains conversation history during the session.

- **🧹 Clear Chat Functionality**
  - One-click Clear Chat button
  - Resets conversation history using Streamlit session state
  
- **Simple & Interactive UI**
  - Built with Streamlit for fast prototyping.

---

## 🧠 Tech Stack

- **Python**
- **Streamlit** – Frontend UI
- **Google Generative AI (Gemini)** – Text & Vision models
- **Pillow (PIL)** – Image handling
- **PyPDF** – PDF text extraction

---

## 📁 Project Structure

```text
├── app.py               # Main Streamlit application
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation

---
