# 🌐 Language Detection, Translation & Summarization Web App

This is a professional-grade **Flask web application** that allows users to:

- 🔍 Automatically detect the input language
- 🌎 Translate text into 20+ supported languages using a trained ML model (not Google API)
- 🧠 Summarize translated text using Hugging Face Transformers
- 🎤 Convert speech-to-text and listen to translated output via text-to-speech
- 📥 Download translated results
- 🌙 Toggle dark/light theme with cookie memory

---

## 💡 Features

- ✅ **Language Detection** (via trained scikit-learn model)
- ✅ **Text Translation** to multiple languages
- ✅ **Text Summarization** after translation
- ✅ **Speech-to-Text** (input by microphone)
- ✅ **Text-to-Speech** (audio output of translation)
- ✅ **Download Translated Text**
- ✅ **Dark Mode Toggle** with cookie storage
- ✅ **Responsive & Animated UI** using Bootstrap 4 + FontAwesome

---

## 📁 Project Structure

```bash
📦 language-translator-app/
├── app.py                  # Flask backend application
├── requirements.txt        # Python dependencies
├── Procfile                # Gunicorn process startup (for Render)
├── render.yaml             # Optional Render deployment config
├── model.pkl               # Trained ML model for language translation
├── vectorizer.pkl          # TF-IDF or similar vectorizer
├── templates/
│   └── index.html          # Frontend interface
├── README.md               # Project documentation




🚀 Local Setup Instructions
1. Clone the repository
git clone https://github.com/Singhrahul2511/language-translator-app.git
cd language-translator-app
2. (Optional) Create and activate virtual environment
python -m venv .venv
.venv\Scripts\activate       # On Windows
source .venv/bin/activate    # On Linux/Mac
3. Install required packages
pip install -r requirements.txt -f https://download.pytorch.org/whl/cpu/torch_stable.html
4. Run the Flask app locally
python app.py
Open your browser and go to:
🔗 http://127.0.0.1:5000

🌐 Deploy to Render (Free Cloud Hosting)
🛠️ Files required:
requirements.txt

Procfile

(optional) render.yaml

🧭 Steps:
Push your code to a GitHub repository

Go to https://render.com

Click New Web Service

Choose your repo

Set:

Build command: pip install -r requirements.txt

Start command: gunicorn app:app

📦 Example Procfile
web: gunicorn app:app
📦 Example render.yaml
services:
  - type: web
    name: language-translator-app
    runtime: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn app:app
    envVars:
      - key: FLASK_ENV
        value: production
🖼️ Features Demo (Screenshots) (optional)
You can add images in a /demo folder and link them like:

![Language Detection](demo/lang_detect.png)
![Translation Result](demo/translation.png)
![Dark Mode](demo/translated_file downloader.png)
🛠️ Built With
Flask

scikit-learn

transformers (Hugging Face)

gTTS / pyttsx3

SpeechRecognition

Bootstrap 4

Font Awesome

👨‍💻 Author
Rahul Kumar
📧 aiwithrahul25@gmail.com
🔗 LinkedIn
🎥 YouTube: AI with Rahul

