# 🎙️ Jarvis Lite

A lightweight Python Voice Assistant that performs **Speech-to-Text (STT)** and **Text-to-Speech (TTS)**. It listens to microphone input, transcribes it using Google's Speech API, and responds with a synthesized robotic voice.



## 🚀 Features

* **Wake Word Detection:** Starts listening when you run the script.
* **Speech Recognition:** Uses the Google Speech Recognition API for high-accuracy transcription.
* **Text-to-Speech:** Offline voice synthesis using `pyttsx3` (works without internet).
* **Command Loop:** Continuously listens until you say "Exit" or "Stop".

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **Hearing:** `SpeechRecognition` library.
* **Speaking:** `pyttsx3` (Python Text-to-Speech version 3).
* **Audio Driver:** `PyAudio` (Low-level microphone access).

## ⚙️ Installation

### 1. Prerequisites (Important!)
You must have a working microphone.

**Windows Users:**
If `pip install pyaudio` fails, you may need to install it manually using pipwin:
```bash
pip install pipwin
pipwin install pyaudio