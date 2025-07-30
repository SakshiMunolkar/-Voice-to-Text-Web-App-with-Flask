from flask import Flask, render_template, jsonify, send_file
import os
import speech_recognition as sr
import pyttsx3

app = Flask(__name__)

# Initialize TTS engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

@app.route('/')
def home():
    text = ""
    if os.path.exists("output.txt"):
        with open("output.txt", "r") as f:
            text = f.read()
    return render_template('index.html', text=text)

@app.route('/record', methods=['POST'])
def record():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("🎤 Listening...")
        audio = r.listen(source)
        print("✅ Processing...")

    try:
        text = r.recognize_google(audio)
        with open('output.txt', 'w') as f:
            f.write(text)
        speak(f"You said: {text}")
        return jsonify({"status": "success", "text": text})
    except sr.UnknownValueError:
        return jsonify({"status": "error", "message": "Could not understand audio"})
    except sr.RequestError:
        return jsonify({"status": "error", "message": "Google Speech service unavailable"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

@app.route('/download')
def download():
    file_path = 'output.txt'
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    return "No file to download", 404

if __name__ == "__main__":
    app.run(debug=True)
