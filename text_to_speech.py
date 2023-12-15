import pyttsx3

def text_to_speech(text):
      # Define the message to be spoken inside the function
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 70)  # Set the speech rate (70 less than the default rate)
    engine.say(text)
    engine.runAndWait()

#text_to_speech("hello")
