# 🤖 Kevin - Gemini Terminal Chatbot Assistant

Welcome to **Kevin**, a terminal-based chatbot assistant developed using **Google's Gemini API (Generative AI)**. This chatbot is tailored to respond as **Kevin**, the friendly principal of AV Group of Institutions, helping users clarify queries specifically related to the institution.

## 📌 Project Overview

This chatbot was developed as part of the **TM Nexus Hub's First Workshop**, conducted by **Tharvesh Muhaideen A**.

- **Language:** Python  
- **Interface:** Terminal/Console  
- **API Used:** Google Generative AI (Gemini 1.5 Flash)  
- **Character Role:** Principal Kevin – Answers institution-specific queries  

> 🛑 The chatbot is restricted to institutional topics only. If a user asks an unrelated question, it politely declines with:  
> _“Sorry, I can't help with that.”_

---

## 🚀 How It Works

1. User types a question in the terminal.
2. Kevin (Gemini AI) processes the input and responds according to the system prompt.
3. If the input is not related to the AV Group of Institution, the chatbot declines to answer.

---

## 🧠 AI Configuration

- **Temperature:** 0.5 *(Balanced thinking)*  
- **Top-p:** 0.95  
- **Top-k:** 64  
- **Max Output Tokens:** 1000  
- **Model:** `gemini-1.5-flash`

---

## 🔧 Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/TM-Nexus-Hub/Projects.git
   cd "gAI with Python"
   Install dependencies:
   pip install google-generativeai
   ```

2. Add your API key: Replace the placeholder in app.py:
   ```python
   api_key = "Replace with your api"
   ```

3. Run the chatbot:
   ```bash
   python app.py
   ```


## 👨‍💻 Author
Tharvesh Muhaideen A
[GitHub](https://github.com/tharvesh588) • [LinkedIn](https://linkedin.com/in/tharvesh2005) • TM Nexus Hub | [Github](https://github.com/TM-Nexus-Hub) | [Instagram](https://instagram.com/tmnexus.official)

## 📄 License
This project is open-sourced under the <strong>[MIT License](../LICENSE).</strong>


## 🏷️ Tags
`#Python` `#GeminiAPI` `#Chatbot` `#TMNexusHub` `#TerminalApp` `#WorkshopProject`
