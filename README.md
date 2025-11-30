AI HR ASSISTANT (Flask-Based Project)


📌 Overview

This project is an AI-powered HR Assistant built using Flask and Google’s Gemini AI model.
It works like a virtual HR representative that can:

Answer general HR questions

Explain company leave policy

Provide professional HR-style replies

Handle leave requests

Respond politely in a conversational format

The system is lightweight, fast, and works entirely through a web interface (HTML + CSS + JS + Flask).


⚡ Features

✔ AI Chatbot

Provides natural HR-style responses using Gemini 2.5 Flash.

✔ Leave Request Submission

Employees can enter:

Name

Employee ID

From date

To date

Reason

The system verifies it and returns a formatted leave confirmation.

✔ Clean Frontend

Simple HR panel-like UI:

Chat window

Leave form

Instant response rendering

✔ Modular Flask Backend

Clearly separated routes:

/ → homepage

/chat → chatbot API

/submit_leave → leave submission

✔ Error Handling

If API key is wrong or model unavailable, a friendly HR error is shown.

⚠ Limitations

No database connected (demo version).

No authentication (anyone can use).

Does not store employee leave history.

Works only with a valid Google Generative AI API key.

Not yet customized for specific company policies.

🧰 Tech Stack
Frontend

HTML

CSS

JavaScript

Backend

Python

Flask

AI

Google Generative AI – Gemini 2.5 Flash

google-generativeai Python library

🔐 APIs & Models Used
Component	Details
AI Model	models/gemini-2.5-flash
Python Package	google-generativeai
Response Method	model.generate_content()
Framework	Flask
🛠️ Setup & Run Instructions
1️⃣ Clone the repository
git clone https://github.com/yourname/AI-HR-Flask.git
cd AI-HR-Flask

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Add your API key

Open app.py and replace:

genai.configure(api_key="YOUR_API_KEY")


OR store it safely as environment variable:

set GOOGLE_API_KEY="your_key"

4️⃣ Run the Flask app
python app.py

5️⃣ Open in browser
http://127.0.0.1:5000


You can now chat with the HR bot or submit a leave request.

🚀 Potential Improvements

These can be added in future versions:

🔹 Add Database (MySQL / Firebase / MongoDB)

Store leave history

Store employee profiles

🔹 Add Authentication

Login for employees

Admin/HR dashboard

🔹 Add built-in HR knowledge base

Policies

Rules

Benefits

Attendance

🔹 Add file upload for leave documents

(PDF, medical certificates, proof, etc.)

🔹 Deploy on Cloud

Render

Vercel

PythonAnywhere
