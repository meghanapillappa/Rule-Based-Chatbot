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
        elif "time" in user_input:
            from datetime import datetime
            print("ChatBot: The current time is", datetime.now().strftime("%H:%M:%S"))
        elif "date" in user_input:
            from datetime import datetime
            print("ChatBot: Today's date is", datetime.now().strftime("%Y-%m-%d"))
        elif "who made you" in user_input:
            print("ChatBot: I was created as part of a Python internship task.")
        elif "what can you do" in user_input:
            print("ChatBot: I can chat with you, tell time, date, and answer simple questions!")
        elif "thank you" in user_input or "thanks" in user_input:
            print("ChatBot: You're welcome! 😊")
        elif "weather" in user_input:
            print("ChatBot: I can't check live weather yet 🌦️, but you can ask me general questions.")
        elif "joke" in user_input:
            print("ChatBot: Why did the computer go to the doctor? Because it caught a virus 😂")
        else:
            print("ChatBot: Sorry, I don't understand that yet.")

# Run chatbot
if __name__ == "__main__":
    chatbot()
