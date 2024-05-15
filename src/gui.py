import tkinter as tk
from tkinter import scrolledtext, Canvas
import time

class AnimatedIndicator:
    def __init__(self, canvas):
        self.canvas = canvas
        self.shape = canvas.create_oval(10, 10, 60, 60, fill='blue')
        self.animating = False

    def start_animation(self):
        if not self.animating:
            self.animating = True
            self.animate()

    def stop_animation(self):
        self.animating = False

    def animate(self):
        if self.animating:
            for _ in range(5):
                self.canvas.move(self.shape, 0, -5)
                self.canvas.update()
                time.sleep(0.05)
            for _ in range(5):
                self.canvas.move(self.shape, 0, 5)
                self.canvas.update()
                time.sleep(0.05)
            self.canvas.after(100, self.animate)  # Re-trigger the animation

class ChatbotGUI:
    def __init__(self, master, input_handler):
        ...
        self.canvas = Canvas(master, width=200, height=100, bg='white')
        self.canvas.grid(column=0, row=1, columnspan=2, pady=10)
        self.animated_indicator = AnimatedIndicator(self.canvas)
        ...

    def activate_chatbot(self):
        self.animated_indicator.start_animation()  # Start animation on activity
        self.input_handler(self)  # Assume this will call a function that eventually stops the animation

    def update_chat_history(self, message):
        self.text_area.config(state=tk.NORMAL)
        self.text_area.insert(tk.END, message + "\n")
        self.text_area.config(state=tk.DISABLED)
        self.text_area.yview(tk.END)
        self.animated_indicator.stop_animation()  # Stop animation when done


def main():
    root = tk.Tk()
    root.geometry("400x300")  # Set the window size
    gui = ChatbotGUI(root, lambda x: None)  # Placeholder for the input handler function
    root.mainloop()

if __name__ == "__main__":
    main()
