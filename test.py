import speech_recognition as sr
from gtts import gTTS
import playsound
from time import ctime
import webbrowser
import time
import os
import random


os.environ["ALSA_LOG_LEVEL"] = "none"
r = sr.Recognizer()


def recognize_audio(ask=False):
    if ask:
        mandakini_speak(ask)
    with sr.Microphone() as source:
        audio = r.listen(source)
        voice_data = ""
        try:
            voice_data = r.recognize_google(audio, language="en-US")
        except sr.UnknownValueError:
            mandakini_speak("Sorry you were not audible")
        return voice_data


def mandakini_speak(audio_str):
    tts = gTTS(text=audio_str, lang="en")
    r = random.randint(1, 1000000)
    audio_file = "audio-" + str(r) + ".mp3"
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_str)
    os.remove(audio_file)


def respond_audio(voice_data):
    if "what is your name" in voice_data:
        mandakini_speak("My name is mandakini")
    if "what is the time now" in voice_data:
        mandakini_speak(f"The time now is {ctime()}")
    if "search" in voice_data:
        search = recognize_audio("What do you want to search?")
        url = "https://google.com/search?q=" + search
        webbrowser.get().open(url)
        mandakini_speak("Here is what I found for your search" + search)
    if "find location" in voice_data:
        maps = recognize_audio("Which location you want to find?")
        url = "https://google.com/maps?q=" + maps
        webbrowser.get().open(url)
        mandakini_speak(f"Your search for the location {maps} is here: ")
    if "thanks" in voice_data:
        exit()

    return voice_data


time.sleep(1)
mandakini_speak("How can I help you?")
while 1:
    data = recognize_audio()
    print(data)

    respond_audio(data)
