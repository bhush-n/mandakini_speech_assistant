
# 🧠 Mandakini - A Python Voice Assistant

Mandakini is a simple yet powerful voice assistant built using Python. It listens to your voice, understands commands, responds with speech, and performs tasks like Google search, telling time, and locating places on Google Maps.

---

## ✨ Features

- 🎤 Voice recognition (Google STT)
- 🔊 Text-to-Speech responses (Google TTS)
- ⏰ Tells current system time
- 🔎 Performs Google searches
- 📍 Finds locations on Google Maps
- 🗣️ Fully interactive via microphone
- 🎯 Lightweight and beginner-friendly

---

## 🛠️ Prerequisites

Ensure Python 3.7+ is installed. Also, you'll need microphone access on your system.

### 📦 Required Python Packages

Install dependencies via `pip`:

```bash
pip install SpeechRecognition gTTS playsound
````

### 🔧 System-Specific Notes

#### For Linux:

```bash
sudo apt install portaudio19-dev
pip install pyaudio
```

#### For Windows:

* Install PyAudio from: [https://www.lfd.uci.edu/\~gohlke/pythonlibs/#pyaudio](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)
* Use `pip install path/to/downloaded.whl`

---

## 🚀 Installation

1. Clone the repository or create a project directory:

```bash
mkdir voice_assistant
cd voice_assistant
```

2. Create the main script:

```bash
touch mandakini.py
```

3. Copy the code from below into `mandakini.py`.
---

## 🧪 How to Use

Run the assistant from your terminal:

```bash
python mandakini.py
```

Then speak one of the following:

| Command Example         | Response / Action                        |
| ----------------------- | ---------------------------------------- |
| “What is your name?”    | Says "My name is mandakini"              |
| “What is the time now?” | Tells the current system time            |
| “Search”                | Asks what to search and opens Google     |
| “Find location”         | Asks what location and opens Google Maps |
| “Thanks”                | Says goodbye and exits                   |

> 📝 Speak clearly and allow a second or two between prompts.

---

## 💡 Future Enhancements

* 🔐 Add wake-word support ("Hey Mandakini")
* 📴 Offline mode using `pyttsx3` for speech
* 📅 Add reminders with Google Calendar API
* 🧾 Logging and saving voice commands
* 🧠 AI-powered intent detection using NLP
* 🧩 GUI version with Tkinter or PyQt

---

## 📚 License

MIT License. Feel free to fork and modify.

---

## 🤖 Built With

* Python 3
* [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
* [gTTS](https://pypi.org/project/gTTS/)
* [playsound](https://pypi.org/project/playsound/)
* `webbrowser`, `ctime`, `os`, `random`

---

## 👋 Author

Made with ❤️ by [Bhushan](https://github.com/bhush-n)
Connect & contribute your own features!

---
