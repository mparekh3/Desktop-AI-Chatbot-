import tkinter as tk
from gui import ChatbotGUI
from speech_recognition_utils import listen_speech
from text_to_speech_utils import speak
from chatbot_model import generate_response

def handle_user_input(gui):
    """Handles the flow from listening to responding."""
    try:
        input_text = listen_speech()  # Listen for user's speech
        if input_text:
            gui.update_chat_history(f"You: {input_text}")
            response_text = generate_response(input_text)  # Generate a response
            gui.update_chat_history(f"Chatbot: {response_text}")
            speak(response_text)  # Speak out the response
        else:
            gui.update_chat_history("No input detected. Please try again.")
    except Exception as e:
        print(f"An error occurred: {e}")
        gui.update_chat_history(f"Error: {str(e)}")

def main():
    root = tk.Tk()
    gui = ChatbotGUI(root, handle_user_input)  # Pass the handler function to GUI
    root.mainloop()

if __name__ == "__main__":
    main()
