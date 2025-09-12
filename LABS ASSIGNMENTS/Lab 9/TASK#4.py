### 2. `chatbot.py`
"""
Chatbot Application
Lab 9 – Task 4
"""

# Predefined responses stored in a dictionary
responses = {
    "hello": "Hi there! How can I help you?",
    "what is your name": "I am your friendly Python chatbot.",
    "bye": "Goodbye! Have a nice day."
}


def chatbot_response(user_input):
    """
    Returns chatbot's response based on user input.
    
    Args:
        user_input (str): The message typed by the user.
    
    Returns:
        str: Chatbot's reply (predefined) or default message if not found.
    """
    # Normalize input by converting to lowercase and stripping spaces
    cleaned_input = user_input.lower().strip()

    # Match user input with predefined responses
    if cleaned_input in responses:
        return responses[cleaned_input]
    
    # If input is unknown, return a default response
    return "Sorry, I don’t understand that."


if __name__ == "__main__":
    print("Welcome to the Chatbot! Type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        
        # Get chatbot reply
        reply = chatbot_response(user_input)
        print("Chatbot:", reply)

        # Exit loop if user types 'bye'
        if user_input.lower().strip() == "bye":
            break
