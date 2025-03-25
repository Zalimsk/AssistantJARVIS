import rasa
from rasa.core.agent import Agent
from rasa.core.interpreter import RasaNLUInterpreter
from transformers import pipeline
import nltk
from nltk.chat.util import Chat, reflections

# Load NLTK chat patterns
def load_nltk_chat():
    pairs = [
        (r"hi|hello", ["Hello!", "Hi there!"]),
        (r"what is your name?", ["I am a chatbot created using NLTK."]),
        (r"quit", ["Bye!"]),
    ]
    return Chat(pairs, reflections)

# Load Transformers model
def load_transformers_model():
    return pipeline("conversational")

# Load Rasa agent
def load_rasa_agent():
    interpreter = RasaNLUInterpreter("models/nlu")
    agent = Agent.load("models/dialogue", interpreter=interpreter)
    return agent

# Function to get a response from Rasa
async def get_rasa_response(agent, message):
    responses = await agent.handle_text(message)
    return responses[0]['text']

# Function to get a response from Transformers
def get_transformers_response(model, message):
    return model(message)[0]['generated_text']

# Function to get a response from NLTK
def get_nltk_response(chatbot, message):
    return chatbot.respond(message)

async def main():
    # Initialize NLTK, Transformers, and Rasa
    nltk_chatbot = load_nltk_chat()
    transformers_model = load_transformers_model()
    rasa_agent = load_rasa_agent()

    while True:
        message = input("You: ")
        
        if 'exit' in message.lower() or 'quit' in message.lower():
            print("Chatbot: Goodbye! Have a great day!")
            break

        # Get response from Rasa
        rasa_response = await get_rasa_response(rasa_agent, message)
        if rasa_response:
            print(f"Rasa: {rasa_response}")
        else:
            # Get response from Transformers
            transformers_response = get_transformers_response(transformers_model, message)
            if transformers_response:
                print(f"Transformers: {transformers_response}")
            else:
                # Fallback to NLTK response
                nltk_response = get_nltk_response(nltk_chatbot, message)
                print(f"NLTK: {nltk_response}")

if __name__ == "_main_":
    import asyncio
    asyncio.run(main())