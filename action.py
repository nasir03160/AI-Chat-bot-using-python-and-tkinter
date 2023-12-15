from datetime import datetime
import webbrowser
import text_to_speech
import speech_to_text

def Action(data):
    user_data=data.lower()
    user_data = speech_to_text.speech_to_text()
    response = ""

    if "what is your name" in user_data:
        text_to_speech.text_to_speech("My name is AI assistant")
        response = "My name is AI assistant"

    elif "Hello" in user_data or "Hi" in user_data:
        text_to_speech.text_to_speech("Hello, how can I help you?")
        response = "Hello, how can I help you?"

    elif "Good Morning" in user_data:
        text_to_speech.text_to_speech("Good Morning, Sir")
        response = "Good Morning, Sir"

    elif "Tell me the time" in user_data:
        current_time = datetime.now().strftime("%H:%M")
        text_to_speech.text_to_speech(f"The current time is {current_time}")
        response = f"The current time is {current_time}"

    elif "shutdown" in user_data:
        text_to_speech.text_to_speech("Okay, shutting down")
        response = "Shutting down"

    elif "open youtube" in user_data:
        webbrowser.open("https://www.youtube.com/")
        text_to_speech.text_to_speech("YouTube opened")
        response = "YouTube opened"

    else:
        text_to_speech.text_to_speech("I don't understand")
        response = "I don't understand"

    return response

if __name__ == "__main__":
    result = Action()
    print(result)  # Display the response
