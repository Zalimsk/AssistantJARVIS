from transformers import Pipeline, Conversation
import logging

# Configure logging
logging.basicConfig(filename='chatbot_conversations.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def process_input(user_input):
    """Handle edge cases and preprocess user input."""
    if len(user_input.strip()) == 0:
        return "Please enter something."
    # Add more sophisticated text preprocessing here if needed
    return user_input

def filter_response(response):
    """Filter unwanted responses (e.g., offensive content)."""
    # Simple example: Ensure response is not empty
    if not response or "error" in response.lower():
        return "I encountered an issue. Could you please rephrase?"
    return response

def save_conversation(conversation_history):
    """Save conversation history to a log file."""
    with open('chatbot_conversations.log', 'a') as f:
        for role, text in conversation_history:
            f.write(f"{role.upper()}: {text}\n")
        f.write("\n")

def main():
    # Initialize the conversational pipeline with a model suitable for dialogue
    model_name = "facebook/blenderbot-400M-distill"  # Change to other models if needed
    conversational_pipeline = Pipeline("conversational", model=model_name)
    
    conversation_history = []

    print("AI Chatbot: Hi there! Ask me anything. Type 'exit' or 'quit' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("AI Chatbot: Goodbye!")
            save_conversation(conversation_history)
            break
        
        # Process user input
        processed_input = process_input(user_input)
        
        # Append user input to conversation history
        conversation_history.append(("user", processed_input))
        
        # Create a Conversation object with the history
        conversation = Conversation()
        for role, text in conversation_history:
            if role == "user":
                conversation.add_user_input(text)
            else:
                conversation.add_bot_input(text)

        # Generate a response
        conversational_pipeline(conversation)
        
        # Get and filter the AI's response
        response = conversation.generated_responses[-1]
        filtered_response = filter_response(response)
        
        # Print and log the AI's response
        print(f"AI Chatbot: {filtered_response}")
        conversation_history.append(("bot", filtered_response))
        save_conversation(conversation_history)

if __name__ == "__main__":
    main()
