import speech_recognition as sr
import json

def load_config():
    with open('config.json', 'r') as config_file:
        return json.load(config_file)

def listen_speech():
    config = load_config()
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=config['speech_recognition_settings']['ambient_duration'])
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio, language=config['speech_recognition_settings']['language'])
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Could not understand audio")
        return None
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return None

if __name__ == "__main__":
    print("Say something...")
    result = listen_speech()
    if result:
        print("Text captured: " + result)
