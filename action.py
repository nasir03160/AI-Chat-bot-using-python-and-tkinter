from datetime import datetime
import webbrowser
import text_to_speech
import os
import speech_to_text

def open_application(application_path):
    try:
        os.startfile(application_path)
    except Exception as e:
        print(f"Error: {e}")

def Action(data=None):
    if data is None:
        data = speech_to_text.speech_to_text()

    user_data = str(data)
    user_data = user_data.lower()
    response = ""

    if user_data == "" or "what is your name" in user_data:
        text_to_speech.text_to_speech("My name is AI assistant")
        response = "My name is AI assistant"

    elif "hello" in user_data or "hi" in user_data:
        text_to_speech.text_to_speech("Hello, how can I help you?")
        response = "Hello, how can I help you?"

    elif "good morning" in user_data:
        text_to_speech.text_to_speech("Good Morning, Sir")
        response = "Good Morning, Sir"

    elif "tell me the time" in user_data:
        current_time = datetime.now().strftime("%H:%M")
        text_to_speech.text_to_speech(f"The current time is {current_time}")
        response = f"The current time is {current_time}"

    elif "shutdown" in user_data:
        text_to_speech.text_to_speech("Okay, shutting down")
        response = "Shutting down"
        quit()

    elif "open youtube" in user_data:
        webbrowser.open("https://www.youtube.com/")
        text_to_speech.text_to_speech("YouTube opened")
        response = "YouTube opened"

    elif "open stremio" in user_data:
        stremio_path = r'C:\Users\Dell\AppData\Local\Programs\LNV\Stremio-4\Stremio.exe'
        open_application(stremio_path)
        response = "Opened Stremio"

    else:
        text_to_speech.text_to_speech("I don't understand")
        response = "I don't understand"

    return response

if __name__ == "__main__":
    result = Action()
    print(result)  # Display the response
