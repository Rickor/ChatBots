import openai

openai.api_key = "OPENAI_API_KEY"  # Replace with your key

def gpt_bot():
    print(" GPT Chatbot ready! Type 'exit' to quit.")
    while True:
        user_input = input(" You: ")
        if user_input.lower() == "exit":
            print(" Goodbye!")
            break
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}]
        )
        bot_reply = response['choices'][0]['message']['content']
        print(f" AI: {bot_reply}")

# gpt_bot()
