import pyttsx3

def list_voices():
    print("Starting the engine...")
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for i, voice in enumerate(voices):
        print(f"Voice {i}: ID = {voice.id}, Name = {voice.name}, Gender = {voice.gender}, Lang = {voice.languages}")

if __name__ == "__main__":
    list_voices()
