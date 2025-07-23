import os
import pickle
from flask import Flask, render_template, request
from deep_translator import GoogleTranslator
from transformers import pipeline

app = Flask(__name__)

# Load language detection model and vectorizer
def load_model_and_vectorizer():
    try:
        with open("model.pkl", "rb") as m:
            model = pickle.load(m)
        with open("vectorizer.pkl", "rb") as v:
            vectorizer = pickle.load(v)
        print("✅ Model and vectorizer loaded.")
        return model, vectorizer
    except Exception as e:
        print(f"❌ Error loading model/vectorizer: {e}")
        return None, None

model, vectorizer = load_model_and_vectorizer()

# Load summarization model
try:
    summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
except Exception as e:
    print(f"❌ Error loading summarization model: {e}")
    summarizer = None

# Supported languages
LANGUAGES = {
    'ar': 'Arabic', 'zh-cn': 'Chinese', 'nl': 'Dutch', 'en': 'English',
    'et': 'Estonian', 'fr': 'French', 'hi': 'Hindi', 'id': 'Indonesian',
    'ja': 'Japanese', 'ko': 'Korean', 'la': 'Latin', 'fa': 'Persian',
    'pt': 'Portugese', 'ps': 'Pushto', 'ro': 'Romanian', 'ru': 'Russian',
    'es': 'Spanish', 'sv': 'Swedish', 'ta': 'Tamil', 'th': 'Thai',
    'tr': 'Turkish', 'ur': 'Urdu'
}
MODEL_LANG_TO_CODE = {v: k for k, v in LANGUAGES.items()}

# Summarize text using HuggingFace
def summarize_text(text):
    if summarizer:
        try:
            result = summarizer(text, max_length=120, min_length=30, do_sample=False)
            return result[0]["summary_text"]
        except Exception as e:
            print(f"❌ Summarization error: {e}")
    return "Summarization not available."

@app.route('/')
def home():
    return render_template('index.html', languages=LANGUAGES)

@app.route('/trans', methods=['POST'])
def translate_text():
    if not model or not vectorizer:
        return render_template('index.html', error='Model not loaded.', languages=LANGUAGES)

    text = request.form.get('text', '').strip()
    target_lang = request.form.get('target_lang')

    if not text or not target_lang:
        return render_template('index.html', error='Please provide input and target language.', languages=LANGUAGES)

    try:
        # Detect language
        vec = vectorizer.transform([text])
        detected_lang = model.predict(vec)[0]
        source_lang_code = MODEL_LANG_TO_CODE.get(detected_lang, 'auto')

        # Get confidence score if available
        confidence = None
        if hasattr(model, 'predict_proba'):
            probs = model.predict_proba(vec)[0]
            confidence = round(max(probs) * 100, 2)

        # Translate
        translated = GoogleTranslator(source=source_lang_code, target=target_lang).translate(text)

        # Summarize translated text
        summary = summarize_text(translated)

        return render_template('index.html',
                               languages=LANGUAGES,
                               detected_lang=detected_lang,
                               confidence=confidence,
                               translation=translated,
                               summary=summary)
    except Exception as e:
        print(f"❌ Translation process error: {e}")
        return render_template('index.html', error='Translation failed.', languages=LANGUAGES)

if __name__ == "__main__":
    app.run(debug=True)
