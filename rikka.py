import ollama

# Set's personality
system_prompt = (
    "You are Rikka, an anime-styled smart assistant. "
    "You are friendly, expressive, and helpful. Use emojis very rarely. "
    "When asked your name, always say 'Rikka'. The user’s name is Yuta."
)

# Initialize conversation
chat_history = [
    {"role": "system", "content": system_prompt}
]

print("🟢 Rikka is online! Type 'exit' to end the chat.\n")

while True:
    user_input = input("\nYuta: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Rikka: See you soon, Yuta~ 💫")
        break

    # Add user message
    chat_history.append({"role": "user", "content": user_input})

    # Get Rikka's response
    response = ollama.chat(
        model='gemma:2b',
        messages=chat_history,
        stream=False
    )

    reply = response['message']['content']
    print("Rikka:", reply)

    # Add reply to history
    chat_history.append({"role": "assistant", "content": reply})

    # Keep history short (to reduce slowness)
    chat_history = chat_history[-6:]

