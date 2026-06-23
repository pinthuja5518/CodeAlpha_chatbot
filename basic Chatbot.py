def get_chatbot_response(user_input):
    """
    Function to handle the chatbot's rule-based logic.
    Converts input to lowercase to make matching case-insensitive.
    """
    user_input = user_input.strip().lower()
    
    if "hello" in user_input or "hi" in user_input:
        return "Hi!"
    elif "how are you" in user_input:
        return "I'm fine, thanks!"
    elif "bye" in user_input:
        return "Goodbye!"
    else:
        return "I'm sorry, I don't understand that. Try saying 'hello', 'how are you', or 'bye'."

def start_chatbot():
    """
    Main loop function to keep the chatbot running until the user says 'bye'.
    """
    print("Chatbot: Hello! I am a simple rule-based chatbot. (Type 'bye' to exit)")
    
    while True:
        # Taking input from the user
        user_message = input("You: ")
        
        # Getting the predefined response from our function
        bot_response = get_chatbot_response(user_message)
        
        # Outputting the chatbot's reply
        print(f"Chatbot: {bot_response}")
        
        # Breaking the loop if the user wants to leave
        if "bye" in user_message.lower():
            break

# Run the chatbot
if __name__ == "__main__":
    start_chatbot()
    