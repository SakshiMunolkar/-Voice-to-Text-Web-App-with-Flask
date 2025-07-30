Voice-to-Text Web App
A Flask-based web application that converts speech to text using Google Speech Recognition API and gives voice feedback using pyttsx3.

✅ Features
✔ Record your voice using the browser
✔ Convert speech to text with high accuracy
✔ Listen to your spoken text with text-to-speech
✔ Clean and responsive UI using HTML & CSS
✔ Built with Flask + Python

🛠 Technologies Used
Python: Flask, SpeechRecognition, pyttsx3
HTML5 / CSS3
Google Speech Recognition API


Installation & Setup
1. Clone the Repository
 git clone https://github.com/yourusername/voice-to-text-app.git
cd voice-to-text-app

 2. Install Dependencies
bash
Copy
Edit
pip install flask SpeechRecognition pyttsx3 pipwin
pipwin install pyaudio

3. Run the Application
bash
Copy
Edit
python app.py

4. Open in Browser
cpp
Copy
Edit
http://127.0.0.1:5000


📂 Project Structure
csharp
Copy
Edit
voice-to-text-app/
│
├── app.py                # Main Flask application
├── templates/
│    └── index.html       # Frontend UI
└── static/
     └── style.css        # CSS styling

     
✅ How It Works
Click Start Recording

Speak into your microphone

The app converts your speech to text

Text is displayed on the page and read aloud


 Future Enhancements
✅ Multi-language support (English, Hindi, etc.)

✅ Real-time transcription (like Google Docs)

✅ Save and download multiple recordings


 Use Cases
Voice notes

Accessibility tools

AI-based assistants



