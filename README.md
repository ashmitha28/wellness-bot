# wellness-bot
A modern AI-powered wellness coach built with Python, Tkinter, and OpenAI APIs. This desktop app supports both text and voice input/output, offering personalized health and wellness conversations.

---

## ✨ Features

- 🧠 Chat with an AI wellness coach using OpenAI's GPT-3.5
- 🎤 Speak to the bot via microphone (voice-to-text with Whisper API)
- 🔊 Hear responses spoken aloud using OpenAI's TTS voice API
- 💬 Modern chat-style interface with text and audio support
- 🔁 Keeps conversation context throughout the session

---

## 🛠️ Tech Stack

- Python 3.12+
- Tkinter (GUI)
- OpenAI API (GPT, Whisper, TTS)
- PyAudio + wave (voice recording)
- tqdm (recording progress bar)

---

## 🚀 Getting Started

### 1. Clone the repo

git clone https://github.com/your-username/wellness-coach-chatbot.git
cd wellness-coach-chatbot

### 2. how to run
You can run the app locally by running python chatbot.py.

It is worth noting that you should paste your own openai api_key to openai.api_key = "sk-***".

If you want to send a message by typing, feel free to type any questions in the text area then press the "Send" button.

If you want to send a message by talking, feel free to press the "Record" button and ask your question.

If you want the bot to answer you by talking, tick the "is_talk" button.

You can set the time(second) for recording your audio by RECODE_SECONDS, which is set to 5 by default.

Enjoy your chat with the wellness coach, have a good time!
