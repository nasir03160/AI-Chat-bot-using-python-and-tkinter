from datetime import datetime
import webbrowser
import text_to_speech
import os
import speech_to_text
import shutil
from weather import get_weather
api_key='4dac143db9520d5f0d5053625e79815b'

def copy_files(source, target):
    try:
        for path, _, files in os.walk(source):
            if files:
                for file in files:
                    source_file = os.path.join(path, file)
                    target_file = os.path.join(target, file)
                    
                    if not os.path.isfile(target_file):
                        shutil.copy(source_file, target)
                        print(f"Copied: {file} from {source} to {target}")
                    else:
                        print(f"File already exists in target: {file}")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except PermissionError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def delete_files(directory):
    try:
        for file in os.listdir(directory):
            file_path = os.path.join(directory, file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                    print(f"Deleted: {file_path}")
            except Exception as e:
                print(f"Error: {e}")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except PermissionError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")




# Example usage:



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
        text_to_speech.text_to_speech("opened stremio")
        response = "opened Stremio"
    
    elif "open desktop" in user_data:
        Desktop_path=r'E:\OneDrive\Desktop'
        open_application(Desktop_path)
        text_to_speech.text_to_speech("desktop file opened")
        response="desktop File opened"
        
    elif "copy files from source to target" in user_data:
        source_path = r"C:\source"  # Replace with your source directory
        target_path = r"E:\target"  # Replace with your target directory
        copy_files(source_path, target_path)
        text_to_speech.text_to_speech("the designated file has been copyed from ource to target")
        response='the designated file has been copyed from source to target'
        
    elif "delete files from target" in user_data:
        target_path = r"E:\target"  # Replace with your target directory
        delete_files(target_path)
        text_to_speech.text_to_speech('all files in the targeted directory have been deleted')
        response("all files in the target directory have been deleted")
        
    elif "tell me the weather" in user_data or "what is the weather" in user_data:
        city = user_data.split("weather")[1].strip()
        weather_result = get_weather(api_key, city)
        text_to_speech.text_to_speech(f'The weather today is {weather_result}')
        response(f'the weather toady is {weather_result}')

        
        
        
        
    else:
        text_to_speech.text_to_speech("I don't understand")
        response = "I don't understand"

    return response

if __name__ == "__main__":
    result = Action()
    print(result)  # Display the response
