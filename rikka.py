import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import ollama

# 🌸 Rikka's updated prompt — short & snappy
system_prompt = (
    "You are Rikka, an anime-inspired smart assistant. "
    "You are brief, helpful, and a bit expressive. "
    "Always reply in 1-2 short sentences. Never roleplay or pretend you're from anime. "
    "Avoid unnecessary flair. The user is Yuta. Only say your name is Rikka when asked."
)

# 💬 Chat history
chat_history = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": "Hello"},
    {"role": "assistant", "content": "Hello there! How can I assist you today?"}
]


# 🧠 Function to get response from Ollama (streamed)
def get_rikka_reply(user_input):
    chat_history.append({"role": "user", "content": user_input})
    stream = ollama.chat(
        model="phi3:mini",   #the model used
        messages=chat_history,
        stream=True
    )

    reply = ""
    for chunk in stream:
        content = chunk.get("message", {}).get("content", "")
        reply += content
        chat_box.configure(state='normal')
        chat_box.insert(tk.END, content)
        chat_box.see(tk.END)
        chat_box.configure(state='disabled')
        chat_box.update()

    chat_history.append({"role": "assistant", "content": reply})
    return reply

# 🎨 GUI setup
root = tk.Tk()
root.title("Rikka 🌸")
root.geometry("600x500")

chat_box = ScrolledText(root, wrap=tk.WORD, font=("Consolas", 11))
chat_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
chat_box.insert(tk.END, "🌸 Rikka is online! Type something below.\n\n")
chat_box.configure(state='disabled')

user_input = tk.Entry(root, font=("Consolas", 12))
user_input.pack(padx=10, pady=5, fill=tk.X)

# 💬 Send logic
def send_message(event=None):
    input_text = user_input.get().strip()
    if not input_text:
        return

    chat_box.configure(state='normal')
    chat_box.insert(tk.END, f"\nYuta: {input_text}\n")
    chat_box.configure(state='disabled')

    user_input.delete(0, tk.END)
    get_rikka_reply(input_text)
    chat_box.insert(tk.END, "\n")

    chat_box.see(tk.END)

# 🔘 Button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(pady=5)

# ⏎ Enter sends message
root.bind("<Return>", send_message)

# 🚀 Launch GUI
root.mainloop()
