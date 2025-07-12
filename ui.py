from tkinter import Text, Scrollbar, Checkbutton, IntVar, END, WORD
from tkinter import ttk

def setup_ui(base, logic):
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TButton",
        padding=6,
        relief="flat",
        background="#9894E9",
        foreground="white",
        font=("Helvetica", 11, "bold")
    )
    style.map("TButton", background=[("active", "#6C63FF")])

    chat_window = Text(base, bd=0, fg='black', bg="#ffffff", font=("Helvetica", 12), wrap=WORD, padx=10, pady=10)
    chat_window.config(state="disabled")
    scrollbar = Scrollbar(base, command=chat_window.yview)
    chat_window['yscrollcommand'] = scrollbar.set

    entry_box = Text(base, bd=0, bg="#f9f9f9", font=("Helvetica", 12), height=3, wrap=WORD, fg="gray")
    entry_box.insert("1.0", "Start typing here...")

    def clear_placeholder(event):
        if entry_box.get("1.0", "end-1c") == "Start typing here...":
            entry_box.delete("1.0", END)
            entry_box.config(fg="black")

    def restore_placeholder(event):
        if entry_box.get("1.0", "end-1c").strip() == "":
            entry_box.insert("1.0", "Start typing here...")
            entry_box.config(fg="gray")

    entry_box.bind("<FocusIn>", clear_placeholder)
    entry_box.bind("<FocusOut>", restore_placeholder)

    talk_var = IntVar()
    logic.set_ui_refs(chat_window, entry_box, talk_var)

    send_button = ttk.Button(base, text="Send", command=logic.send_text)
    audio_button = ttk.Button(base, text="🎤  Record", command=logic.send_audio)
    clear_button = ttk.Button(base, text="Clear", command=logic.clear_chat)
    talk_check = Checkbutton(base, text="🎶 Voice Output", variable=talk_var, bg="#f0f4f7", font=("Helvetica", 14))

    # Layout
    scrollbar.place(x=675, y=6, height=360)
    chat_window.place(x=10, y=6, height=360, width=665)
    entry_box.place(x=10, y=375, height=100, width=560)
    send_button.place(x=580, y=375, height=30, width=100)
    audio_button.place(x=580, y=410, height=30, width=100)
    clear_button.place(x=580, y=445, height=30, width=100)
    talk_check.place(x=10, y=485)

    base.protocol("WM_DELETE_WINDOW", logic.exit_app)
