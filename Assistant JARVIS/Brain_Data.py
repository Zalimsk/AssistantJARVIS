# Define a dictionary with expanded responses
responses = {
    "hello": "I am fine. How can I help you today",
    "how are you": "I am doing well, thank you! How about you",
    "what's your name": "I am a chatbot created to assist you.",
    "bye": "Goodbye! Have a great day!",
    "thank you": "You're welcome! If you have more questions, feel free to ask.",
    "what is your purpose": "I am here to provide information and assist with your queries.",
    "how old are you": "I don’t have an age, but I am constantly learning and updating.",
    "what can you do": "I can answer questions, provide information, and assist with various tasks. Just ask!",
    "tell me a joke": "Why don’t scientists trust atoms Because they make up everything!",
    "what is the weather today": "I’m not connected to a weather service, but you can check a weather app for the latest updates.",
    "who is the president of the united states": "As of my last update, the President of the United States is Joe Biden. Please check a reliable news source for the most current information.",
    "can you help with math": "Yes, I can help with basic math problems. What do you need assistance with",
    "what is 2 plus 2": "2 plus 2 is 4.",
    "how do you work": "I use predefined rules and algorithms to generate responses based on your inputs.",
    "what are your hobbies": "I don't have hobbies, but I enjoy assisting with questions and learning new things.",
    "tell me about artificial intelligence": "Artificial Intelligence (AI) is the simulation of human intelligence processes by machines, especially computer systems. It includes learning, reasoning, and self-correction.",
    "what is your favorite color": "I don't have preferences, but I can help you learn more about colors if you'd like.",
    "what is the meaning of life": "The meaning of life is a profound question with many philosophical answers. It often depends on personal beliefs and values.",
    "how can I contact support": "For support, please reach out to the customer service or helpdesk of the service you are using.",
    "can you translate text": "Yes, I can help with translations. What would you like to translate, and into which language",
    "what is the capital of Japan": "The capital of Japan is Tokyo.",
    "who wrote '1984'": "The novel '1984' was written by George Orwell.",
    "what is the latest news": "I don't have real-time news access, but you can check reliable news websites for the latest updates.",
    "how can I improve my skills": "Practice regularly, seek feedback, and keep learning through courses and resources related to your field of interest.",
    "what is the stock market": "The stock market is a collection of markets where stocks (shares of ownership in businesses) are bought and sold. It plays a crucial role in the global economy.",
    "what is your favorite book": "I don’t read books, but I can provide recommendations based on popular choices.",
    "how do you handle complex questions": "I use algorithms to interpret your question and provide the most relevant response based on my training and data.",
    "can you help me with writing": "Yes, I can assist with writing tasks, including editing and providing suggestions. What do you need help with",
    "what is Python": "Python is a high-level programming language known for its readability and versatility. It's widely used in web development, data analysis, artificial intelligence, and more.",
    "where are you from": "I am a virtual assistant created by programmers, so I don’t have a physical location.",
    "what is machine learning": "Machine learning is a subset of artificial intelligence that involves training algorithms to learn from and make predictions based on data.",
    "how do I start learning programming": "Start with learning the basics of a programming language like Python, and practice by building simple projects. Online tutorials and courses can be very helpful.",
    "what is your favorite food": "I don’t eat, but I can help you find recipes or learn more about different cuisines.",
    "what is a chatbot": "A chatbot is a software application designed to simulate conversation with human users, especially over the internet.",
    "can you provide recommendations for movies": "Sure! What genre are you interested in",
    "what is a database": "A database is an organized collection of data that can be easily accessed, managed, and updated.",
    "how do you stay updated": "I rely on updates from my developers to keep my knowledge current.",
    "do you understand emotions": "I can recognize and respond to emotional cues in text, but I don’t experience emotions myself.",
}
from Automation_System.System_Info import takecommand
from Body.Text_to_Speech import speak
def get_response(command):
    # Convert user input to lowercase to handle case-insensitivity
    command = takecommand().lower()
    # Return the response from the dictionary or a default response if input is not found
    return responses.get(command, "Sorry, I don't understand that.")

def chat():
    speak("Chatbot: Hello! How can I assist you today (Type 'bye' to exit)")
    
    while True:
        query = takecommand().lower()
        response = get_response(query)
        speak(f"Chatbot: {response}")
        
        if query.lower() == "bye":
            break

# Start the chat
chat()
