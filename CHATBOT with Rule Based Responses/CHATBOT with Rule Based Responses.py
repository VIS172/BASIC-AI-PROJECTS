def chatbot_response(user_input):
    user_input = user_input.lower()  # Convert input to lowercase for case-insensitive matching
    
    # Define rules and responses
    if 'hello' in user_input or 'hi' in user_input or 'hey' in user_input:
        return 'Hello! How can I help you today?'
    elif 'how are you' in user_input:
        return 'I am just a chatbot, but I am here to assist you!'
    elif 'what is your name' in user_input:
        return 'I am a simple rule-based chatbot. You can call me Chatbot!'
    elif 'what can you do' in user_input:
        return 'I can answer simple questions and have a basic conversation with you.'
    elif 'bye' in user_input or 'goodbye' in user_input:
        return 'Goodbye! Have a great day!'
    elif 'help' in user_input:
        return 'Sure! I am here to help. You can ask me things like "what is your name?" or "how are you?".'
    elif 'thank you' in user_input or 'thanks' in user_input:
        return 'You’re welcome! If you have any other questions, feel free to ask.'
    else:
        return 'I am sorry, I did not understand that. Can you please rephrase?'

def chat():
    print("Chatbot: Hello! I am a simple chatbot. Type 'bye' to exit the chat.")
    while True:
        user_input = input("You: ")
        if 'bye' in user_input.lower() or 'goodbye' in user_input.lower():
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chat()
    