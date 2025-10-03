# Rule-Based Chatbot (Task 8)

def chatbot():
    print("Hello! I’m ChatBot 🤖. Type 'exit' to quit.")
    
    while True:
        user_input = input("You: ").lower()

        if user_input == "exit":
            print("ChatBot: Goodbye! Have a nice day 👋")
            break
        elif "hello" in user_input or "hi" in user_input:
            print("ChatBot: Hello there! How can I help you?")
        elif "how are you" in user_input:
            print("ChatBot: I'm just a bot, but I'm doing great! Thanks for asking 😊")
        elif "your name" in user_input:
            print("ChatBot: I'm ChatMini, your friendly assistant.")
        elif "help" in user_input:
            print("ChatBot: Sure! I can answer basic questions. Try asking about me.")
        elif "bye" in user_input:
            print("ChatBot: Bye! Take care.")
            break
        else:
            print("ChatBot: Sorry, I don't understand that yet.")

# Run chatbot
if __name__ == "__main__":
    chatbot()
