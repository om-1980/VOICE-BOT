# Intelligent Voice Bot

## 🚀 Overview
The **Intelligent Voice Bot** is an AI-powered chatbot that supports both text and voice interactions. It utilizes Natural Language Understanding (NLU) to detect user intent, extract entities, and generate responses using text-to-speech. The chatbot also features a modern GUI with interactive elements, database logging, and a real-time typing indicator.

## ✨ Features
- 🎙️ **Speech-to-Text**: Converts voice input to text.
- 🧠 **NLU Processing**: Detects intent and extracts entities.
- 🗣️ **Text-to-Speech**: Responds using synthesized voice.
- 🎨 **Advanced GUI**: User-friendly, dark-mode interface with placeholders and interactive buttons.
- 📜 **Database Logging**: Stores interactions for analysis.
- 🔄 **Real-time Typing Indicator**: Simulates bot response time.

## 📂 Project Structure
```
voice_bot/
│── backend.py             # Database initialization & logging
│── nlu.py                 # Intent detection & entity extraction
│── response_generator.py   # Generates bot responses
│── speech_to_text.py       # Converts speech to text
│── text_to_speech.py       # Converts text to speech
│── gui.py                 # GUI interface
│── app.py                 # Main application script
│── requirements.txt       # Required dependencies
│── README.md              # Project documentation
│── assets/                # Icons & images
│── database/              # SQLite database storage
```

## 🛠️ Installation & Setup
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/yourusername/voice_bot.git
cd voice_bot
```
### 2️⃣ Create Virtual Environment & Install Dependencies
```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```
### 3️⃣ Run the Application
```sh
python gui.py
```

## 🎤 How It Works
1. **Start the bot**.
2. **Type or speak your query**.
3. The bot **processes intent & entities**.
4. The bot **responds via text and voice**.
5. **Interaction is logged** in the database.

## 🛑 Exit
Click the **Exit** button or type **exit** to close the application.

## 📌 Dependencies
- Python 3.8+
- SpeechRecognition
- Transformers (Hugging Face)
- pyttsx3 (Text-to-Speech)
- tkinter (GUI)
- SQLite3 (Database)

## 🤖 Future Enhancements
- ✨ Multilingual Support
- 🏆 Voice Assistant Integration
- 🔍 Improved NLU with deep learning

## 📜 License
MIT License. Feel free to modify and enhance! 🎉

