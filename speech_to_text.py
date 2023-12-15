# Install speech recognition and pyaudio libraries if not already installed

import speech_recognition as sr

def speech_to_text():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("Recognized text:", text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Error: {e}")

speech_to_text()
