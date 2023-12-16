import speech_recognition as sr
import action  # Assuming your action module is named 'action'

def speech_to_text():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("Recognized text:", text)
        return text  # Return the recognized text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return None
    except sr.RequestError as e:
        print(f"Error: {e}")
        return None

def ask():
    user_val = speech_to_text()  # Call the speech_to_text function
    bot_val = action.Action(user_val)
    text.insert(end, 'User ---> ' + user_val + "\n")
    if bot_val is not None:
        text.insert(END, "Bot ---> " + str(bot_val) + '\n')
    if bot_val == "Okay, shutting down":
        root.destroy()

# Assuming 'text' is a Text widget, 'entry' is an Entry widget, and 'END' is properly defined
# Make sure to call the 'ask' function when the "Ask" button is clicked
# For example, if you're using a Button widget:
# ask_button = Button(root, text="Ask", command=ask)
