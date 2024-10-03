from flask import Flask, render_template, request
from langdetect import detect
from googletrans import Translator, LANGUAGES

app = Flask(__name__)

def detect_and_translate(text, target_lang):
    # Detect language
    result_lang = detect(text)

    # Translate language
    translator = Translator()
    translate_text = translator.translate(text, dest=target_lang).text

    return result_lang, translate_text

@app.route('/')
def index():
    # Pass LANGUAGES to template
    return render_template('index.html', languages=LANGUAGES)

@app.route('/trans', methods=['POST'])
def trans():
    detected_lang = ""
    translation = ""

    # Check if text input is provided
    if 'text' in request.form and request.form['text'].strip():
        text = request.form['text'].strip()
        target_lang = request.form['target_lang']
        detected_lang, translation = detect_and_translate(text, target_lang)

    return render_template('index.html', detected_lang=detected_lang, translation=translation, languages=LANGUAGES)

if __name__ == '__main__':
    app.run(debug=True)
