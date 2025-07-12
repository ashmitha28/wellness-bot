from tkinter import Tk
from ui import setup_ui
from logic import ChatLogic

if __name__ == "__main__":
    root = Tk()
    root.title("Wellness Coach Chatbot")
    root.geometry("700x550")
    root.configure(bg="#d0e5f4")

    logic = ChatLogic()
    setup_ui(root, logic)

    root.mainloop()
