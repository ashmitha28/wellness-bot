import openai, sys, wave, pyaudio, logging as log
from tqdm import tqdm
from playsound import playsound

openai.api_key = "sk-"  # Replace with your key
log.basicConfig(filename='openai-history.log', encoding='utf-8', level=log.DEBUG)

class ChatLogic:
    def __init__(self):
        self.messages = []
        self.chat_window = None
        self.entry_box = None
        self.talk_var = None

    def set_ui_refs(self, chat_window, entry_box, talk_var):
        self.chat_window = chat_window
        self.entry_box = entry_box
        self.talk_var = talk_var

    def get_audio(self):
        RATE, FORMAT, CHANNELS, CHUNK, RECODE_SECONDS = 16000, pyaudio.paInt16, 1, 1024, 8
        p = pyaudio.PyAudio()
        stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
        frames = [stream.read(CHUNK) for _ in tqdm(range(int(RATE / CHUNK * RECODE_SECONDS)))]
        stream.stop_stream(); stream.close(); p.terminate()
        wf = wave.open("user_audio.wav", "wb")
        wf.setnchannels(CHANNELS); wf.setsampwidth(p.get_sample_size(FORMAT)); wf.setframerate(RATE)
        wf.writeframes(b"".join(frames)); wf.close()

    def chatbot_response(self, msg):
        self.messages.append({"role": "user", "content": msg})
        response = openai.chat.completions.create(model="gpt-3.5-turbo", messages=self.messages)
        return response.choices[0].message.content

    def send_text(self):
        msg = self.entry_box.get("1.0", 'end-1c').strip()
        self.entry_box.delete("0.0", "end")
        if msg:
            self.chat_window.config(state="normal")
            self.chat_window.insert("end", f"You: {msg}\n\n")
            self.chat_window.config(foreground="black", font=("Verdana", 12))
            ans = self.chatbot_response(msg)
            self.chat_window.insert("end", f"Wellness Coach 👩🏻‍💻 : {ans}\n\n")
            self.chat_window.config(state="disabled"); self.chat_window.yview("end")
            if self.talk_var.get():
                speech = openai.audio.speech.create(model="tts-1", voice="nova", input=ans)
                with open("res_audio.mp3", "wb") as f:
                    f.write(speech.content)
                playsound("res_audio.mp3")

    def send_audio(self):
        self.get_audio()
        with open("user_audio.wav", "rb") as f:
            msg = openai.audio.transcriptions.create(model="whisper-1", file=f).text
        self.entry_box.delete("0.0", "end")
        if msg:
            self.chat_window.config(state="normal")
            self.chat_window.insert("end", f"You: {msg}\n\n")
            self.chat_window.config(foreground="black", font=("Verdana", 12))
            ans = self.chatbot_response(msg)
            self.chat_window.insert("end", f"Wellness Coach 👩🏻‍💻 : {ans}\n\n")
            self.chat_window.config(state="disabled"); self.chat_window.yview("end")
            if self.talk_var.get():
                speech = openai.audio.speech.create(model="tts-1", voice="nova", input=ans)
                with open("res_audio.mp3", "wb") as f:
                    f.write(speech.content)
                playsound("res_audio.mp3")

    def clear_chat(self):
        self.chat_window.config(state="normal")
        self.chat_window.delete("0.0", "end")
        self.chat_window.config(state="disabled")

    def exit_app(self):
        sys.exit(0)
