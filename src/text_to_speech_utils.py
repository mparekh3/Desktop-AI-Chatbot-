import pyttsx3
import json

def load_config():
    with open('config.json', 'r') as config_file:
        return json.load(config_file)

def speak(text):
    config = load_config()
    engine = pyttsx3.init()
    engine.setProperty('rate', config['tts_settings']['pyttsx3_settings']['rate'])
    engine.setProperty('volume', config['tts_settings']['pyttsx3_settings']['volume'])
    engine.setProperty('voice', config['tts_settings']['pyttsx3_settings']['voice_id'])
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Hello, this is your Desktop AI Chatbot speaking with the new settings.")
