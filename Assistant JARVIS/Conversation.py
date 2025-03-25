import random

# Define extended categories of responses with more variations
responses = {
    "greetings": [
        "Hi there! How can I assist you today?",
        "Hello! What can I do for you?",
        "Hey! How's it going?",
        "Good morning! How can I help you today?",
        "Good afternoon! What can I assist you with?",
        "Good evening! How may I help you?",
        "Howdy! What can I do for you?",
        "Greetings! How can I be of service?",
        "Not much, just here to help. What’s up with you?",
        "Not much, just the usual. What’s new with you?",
        "Hey there! What can I do for you today?",
        "Hello! How’s your day going so far?",
        "Hi! How's your day treating you?",
        "Greetings! How can I make your day better?",
        "Hi! How are you doing today?",
        "Hello there! What brings you here today?"
    ],
    "farewells": [
        "Goodbye! Have a wonderful day!",
        "See you later! Take care!",
        "You too! Have a great day!",
        "Farewell! Have a great day ahead!",
        "Catch you later! Stay safe!",
        "Bye! It was nice talking to you.",
        "Take care and see you next time!",
        "Until next time! Have a good one.",
        "See you soon! Have a fantastic day!",
        "Goodbye for now! Looking forward to our next chat.",
        "It was great talking to you! See you soon.",
        "Take care! Looking forward to our next conversation.",
        "So long! Have a great day ahead.",
        "Wishing you a wonderful day! Goodbye for now."
    ],
    "thanks": [
        "You're welcome! If you need anything else, just ask.",
        "You're welcome! Happy to help.",
        "Anytime! I'm here if you need more help.",
        "You're very welcome! I'm glad I could help.",
        "No problem at all! If there's anything else, let me know.",
        "Glad I could assist! Feel free to reach out anytime.",
        "You're welcome! Let me know if you need further assistance.",
        "It's my pleasure! Don't hesitate to ask if you need more help.",
        "You’re welcome! Always here to support you.",
        "Happy to help! If you need more assistance, just ask.",
        "No worries! I'm here to help with whatever you need."
    ],
    "questions": [
        "I'm not sure about that. Can you provide more details?",
        "Could you clarify that a bit more?",
        "I don't have information on that. Can you rephrase?",
        "That's a bit unclear. Can you explain further?",
        "I need more context to assist you with that.",
        "Sorry, I didn't quite get that. Could you elaborate?",
        "Can you give me more details so I can better assist you?",
        "I’m not familiar with that. Can you provide more context?",
        "Can you specify what you mean?",
        "I’m not certain about that. Could you provide more information?",
        "Could you give me more specifics on that topic?",
        "I’m unclear about that. Can you explain it differently?"
    ],
    "comments": [
        "That's interesting! Tell me more.",
        "I see! How does that make you feel?",
        "Fascinating! What else can you share?",
        "Hmm, that's an interesting point. What’s your take on it?",
        "Thanks for sharing that! Do you have any more thoughts?",
        "That’s quite a perspective. Can you expand on that?",
        "Very interesting! What led you to that conclusion?",
        "I appreciate your input. What more can you add to this?",
        "That’s a unique view. How did you come to that conclusion?",
        "Interesting point! Could you elaborate a bit more?",
        "I’m intrigued by that. What more can you tell me?",
        "That’s a compelling comment. Can you provide more details?"
    ],
    "jokes": [
        "Why don't scientists trust atoms? Because they make up everything!",
        "How does a penguin build its house? Igloos it together!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "What do you call fake spaghetti? An impasta!",
        "Why did the math book look sad? It had too many problems!",
        "What do you call cheese that isn't yours? Nacho cheese!",
        "Why couldn't the bicycle stand up by itself? It was two-tired!",
        "What do you call a bear with no teeth? A gummy bear!",
        "Why did the golfer bring two pairs of pants? In case he got a hole in one!",
        "What do you get when you cross a snowman and a vampire? Frostbite!",
        "Why did the chicken join a band? Because it had the drumsticks!",
        "What did one ocean say to the other ocean? Nothing, they just waved!"
    ],
    "motivational": [
        "Believe in yourself! You have the power to achieve great things.",
        "Keep pushing forward. Success is just around the corner.",
        "Every day is a new opportunity to grow and improve.",
        "Don't give up. Great things take time.",
        "You are capable of amazing things. Keep going!",
        "Stay positive and keep working towards your goals.",
        "Believe in your dreams and they will become reality.",
        "You’ve got this! Keep striving and never give up.",
        "Every challenge is an opportunity in disguise.",
        "Your only limit is your mind. Think big and achieve!",
        "Success is a journey, not a destination. Keep moving forward.",
        "The only way to achieve the impossible is to believe it is possible."
    ],
    "advice": [
        "Always take time to listen to others. It can make a big difference.",
        "Don't be afraid to ask for help when you need it.",
        "Plan ahead and stay organized. It helps in achieving goals.",
        "Take care of your health; it’s the most valuable asset.",
        "Keep learning and growing. Knowledge is power.",
        "Be kind to yourself and others. Kindness goes a long way.",
        "Set clear goals and work towards them step by step.",
        "Embrace challenges as opportunities for growth.",
        "Manage your time wisely. It’s key to productivity.",
        "Stay curious and keep exploring new interests.",
        "Focus on what you can control and let go of what you can’t.",
        "Be patient with yourself. Progress takes time."
    ],
    "encouragement": [
        "You’re doing great! Keep up the good work.",
        "Don’t lose hope. Every small step counts.",
        "You have the strength to overcome any obstacle.",
        "Keep moving forward, even if it’s just a little bit each day.",
        "Your efforts are making a difference. Stay encouraged!",
        "You’re capable of more than you realize.",
        "Believe in your journey and trust the process.",
        "Keep your spirits high. You’re on the right path.",
        "Every day is a new chance to improve and succeed.",
        "You’ve got what it takes to make it through!",
        "Stay resilient and keep pushing. Your hard work will pay off.",
        "Remember, progress is progress, no matter how small."
    ],
    "reminders": [
        "Remember to take breaks and rest. It’s important for your well-being.",
        "Don’t forget to stay hydrated and eat healthily.",
        "Make sure to balance work and relaxation.",
        "Take a moment to reflect on your progress and celebrate small wins.",
        "Set aside time for activities you enjoy.",
        "Remember, it’s okay to ask for support when needed.",
        "Keep track of your goals and revisit them regularly.",
        "Stay organized to keep your stress levels in check.",
        "Remember to practice self-care and mindfulness.",
        "Don’t forget to stay connected with friends and family.",
        "Prioritize your mental health just as you do your physical health.",
        "Take time to breathe and relax amidst your busy schedule."
    ],
    "sympathy": [
        "I'm sorry to hear that. If you need someone to talk to, I'm here.",
        "That sounds tough. I'm here if you need support.",
        "I’m sorry you’re going through this. How can I help?",
        "It’s okay to feel this way. Let me know if there’s anything I can do.",
        "I understand that this is difficult. If you need anything, just ask.",
        "I’m here for you. Let me know how I can support you during this time.",
        "I’m sorry to hear about your situation. If there’s anything I can do, please let me know.",
        "That must be hard. Remember, you don’t have to go through this alone."
    ],
    "celebration": [
        "Congratulations! You’ve achieved something great!",
        "Well done! Your hard work has really paid off.",
        "Fantastic job! You should be proud of your accomplishment.",
        "Cheers to your success! Celebrate your achievement!",
        "You did it! Time to celebrate your hard-earned success.",
        "Awesome work! You’ve earned this moment of celebration.",
        "Kudos to you! Your dedication has led to this achievement.",
        "Bravo! Your efforts have led to a wonderful result."
    ],
    "food": [
        "Let’s talk about your favorite cuisine. What’s your go-to comfort food?",
        "Have you tried any new recipes lately? Let’s share cooking tips!",
        "What’s the best meal you’ve ever had? Let’s discuss food!",
        "Do you enjoy cooking? Let’s exchange some delicious recipes!",
        "Any favorite restaurants you’d recommend? Let’s talk about food!",
        "Have you ever tried to recreate a restaurant dish at home? Let’s swap ideas!",
        "What’s your opinion on spicy food? Let’s discuss different flavors!",
        "Have you ever had a food adventure? Let’s share our culinary experiences!",
        "Are you a fan of desserts? Let’s discuss our favorite sweet treats!",
        "Do you have any dietary preferences? Let’s talk about food options!",
        "What’s your comfort food on a rainy day? Let’s chat about food cravings!",
        "Have you ever tried a cuisine from a different culture? Let’s explore international flavors!"
    ],
    "movies": [
        "What’s your favorite movie genre? Let’s discuss recent films.",
        "Have you watched any good movies lately? Let’s chat about them!",
        "Who is your favorite actor/actress? Let’s talk about movies!",
        "Do you prefer watching movies at home or at the theater? Let’s discuss!",
        "Have you seen any classic movies? Let’s exchange recommendations!",
        "What’s the most recent movie that left an impression on you? Let’s discuss!",
        "Are you a fan of animated movies? Let’s talk about our favorite animated films!",
        "Have you ever been to a film festival? Let’s share our experiences!",
        "Do you enjoy analyzing movie plots? Let’s discuss the latest twists and turns!",
        "Are you excited about any upcoming movie releases? Let’s talk about our expectations!",
        "Have you watched any movies based on books? Let’s compare the adaptations!"
    ],
    "books": [
        "Do you enjoy reading? Let’s talk about your favorite books.",
        "Have you come across any interesting reads lately? Let’s share recommendations!",
        "Who is your favorite author? Let’s discuss books!",
        "Do you prefer physical books or e-readers? Let’s discuss reading preferences!",
        "Have you read any bestsellers recently? Let’s exchange thoughts!",
        "What’s the last book that kept you up all night? Let’s discuss!",
        "Do you enjoy discussing book characters? Let’s talk about our favorites!",
        "Have you ever read a book that changed your perspective? Let’s share insights!",
        "Do you like to read multiple books at once? Let’s discuss our reading habits!",
        "Have you read any memoirs or biographies? Let’s talk about real-life stories!",
        "Are you part of a book club? Let’s share our club experiences!"
    ],
    "music": [
        "What type of music do you enjoy? Let’s discuss your favorite artists.",
        "Have you discovered any new music recently? Let’s share our playlists!",
        "Do you play any musical instruments? Let’s talk about music!",
        "Are you a fan of live music performances? Let’s discuss our favorite concerts!",
        "Have you attended any music festivals? Let’s share our festival experiences!",
        "Do you prefer listening to music while working or relaxing? Let’s discuss!",
        "Are you into music from different cultures? Let’s explore diverse musical genres!",
        "Have you ever been to a music studio? Let’s talk about behind-the-scenes!",
        "What’s your favorite song lyric? Let’s discuss the power of music!",
        "Do you have a special music playlist for different moods? Let’s share our playlists!",
        "Are you excited about any upcoming music releases? Let’s talk about our expectations!"
    ],
    "sports": [
        "Are you a sports fan? Let’s talk about your favorite teams and athletes.",
        "Have you been following any sports events lately? Let’s discuss!",
        "Do you play any sports yourself? Let’s chat about sports!",
        "What’s your favorite sport to watch? Let’s discuss the excitement of the game!",
        "Have you ever attended a major sports event? Let’s share our experiences!",
        "Do you have a favorite sports rivalry? Let’s discuss the thrill of competition!",
        "Are you into fantasy sports leagues? Let’s talk about strategy and players!",
        "What’s your opinion on sportsmanship? Let’s discuss the values of sports!",
        "Have you ever met a sports celebrity? Let’s talk about memorable encounters!",
        "Do you enjoy playing sports video games? Let’s discuss our gaming experiences!",
        "Are you excited about any upcoming sports tournaments? Let’s discuss our predictions!"
    ],
    "news": [
        "Have you heard any interesting news stories lately? Let’s discuss!",
        "Let’s catch up on current events. What’s happening in the world?",
        "Do you follow any specific news sources? Let’s talk about the news!",
        "What’s your opinion on the latest headlines? Let’s discuss current affairs!",
        "Have you ever been surprised by a breaking news story? Let’s discuss our reactions!",
        "Do you stay updated on local news? Let’s talk about community events!",
        "Are there any news topics that you’re passionate about? Let’s discuss our perspectives!",
        "Have you ever witnessed news reporting in action? Let’s talk about media coverage!",
        "What’s your view on the role of journalism in society? Let’s discuss!",
        "Are you interested in investigative journalism? Let’s share our insights!",
        "Do you think social media has changed how we consume news? Let’s discuss the digital age!"
    ],
    "technology": [
        "Are you interested in technology? Let’s talk about the latest innovations.",
        "Have you tried any new gadgets lately? Let’s discuss technology!",
        "Do you have a favorite tech company? Let’s chat about technology!",
        "What’s your opinion on the future of technology? Let’s discuss trends!",
        "Are there any technological advancements that amaze you? Let’s discuss!",
        "Have you ever attended a tech conference? Let’s talk about industry insights!",
        "Do you enjoy exploring new software applications? Let’s discuss our favorites!",
        "What’s your view on the impact of technology on daily life? Let’s discuss!",
        "Are you curious about emerging tech startups? Let’s share our discoveries!",
        "Have you ever tried coding or programming? Let’s discuss our tech skills!",
        "Do you think AI will revolutionize industries? Let’s discuss the potential!"
    ],
    "history": [
        "Do you enjoy history? Let’s discuss your favorite historical periods.",
        "Have you read any interesting history books lately? Let’s share insights!",
        "What historical events fascinate you the most? Let’s talk about history!",
        "Do you think history repeats itself? Let’s discuss the lessons learned!",
        "Are there any historical figures you admire? Let’s discuss their impact!",
        "Have you ever visited historical landmarks? Let’s share our travel experiences!",
        "Do you enjoy exploring museums? Let’s discuss our favorite exhibits!",
        "What’s your view on how history is taught in schools? Let’s discuss!",
        "Are you interested in ancient civilizations? Let’s explore our curiosity!",
        "Have you ever watched historical documentaries? Let’s discuss our perspectives!",
        "Do you believe in preserving historical artifacts? Let’s discuss cultural heritage!"
    ],
    "science": [
        "Are you interested in science? Let’s discuss fascinating scientific discoveries.",
        "Have you heard about any recent scientific breakthroughs? Let’s chat!",
        "Do you have a favorite branch of science? Let’s talk about science!",
        "What scientific mysteries intrigue you the most? Let’s discuss!",
        "Are there any science experiments you’d like to try? Let’s explore ideas!",
        "Have you ever participated in citizen science projects? Let’s discuss our contributions!",
        "Do you think science fiction can predict future scientific advancements? Let’s discuss!",
        "What’s your opinion on the role of ethics in scientific research? Let’s discuss!",
        "Are you curious about space exploration? Let’s discuss the mysteries of the universe!",
        "Have you ever attended science fairs or expos? Let’s share our experiences!",
        "Do you believe in the importance of science education? Let’s discuss lifelong learning!"
    ],
    "animals": [
        "Are you an animal lover? Let’s discuss your favorite animals.",
        "Have you ever had a pet? Let’s talk about our furry friends!",
        "What’s the most fascinating animal fact you know? Let’s share!",
        "Do you have a favorite animal in the wild? Let’s discuss wildlife!",
        "Have you ever visited an animal sanctuary? Let’s talk about animal conservation!",
        "What’s your opinion on animal rights? Let’s discuss ethical treatment.",
        "Are there any endangered species you’re passionate about? Let’s discuss conservation efforts!",
        "Do you enjoy watching nature documentaries? Let’s discuss our favorite shows!",
        "Have you ever volunteered at an animal shelter? Let’s share our experiences!",
        "Are you interested in learning about new animal species? Let’s discuss biodiversity!",
        "What’s your view on the bond between humans and animals? Let’s discuss companionship!"
    ],
    "travel": [
        "Do you enjoy traveling? Let’s discuss your favorite travel destinations.",
        "Have you been on any memorable trips lately? Let’s share travel stories!",
        "What’s the most adventurous travel experience you’ve had? Let’s discuss!",
        "Do you prefer solo travel or group travel? Let’s discuss travel preferences!",
        "Have you ever traveled to a country with a different culture? Let’s discuss cultural experiences!",
        "What’s your dream travel destination? Let’s talk about bucket-list adventures!",
        "Have you ever explored off-the-beaten-path locations? Let’s share travel tips!",
        "What’s your view on sustainable travel practices? Let’s discuss responsible tourism!",
        "Do you collect souvenirs from your travels? Let’s talk about travel memories!",
        "Have you ever tried local cuisine while traveling? Let’s discuss food adventures!",
        "What’s your favorite mode of transportation while traveling? Let’s discuss travel logistics!"
    ],
    "weather": [
        "How’s the weather where you are? Let’s discuss the climate.",
        "Do you enjoy the changing seasons? Let’s talk about weather patterns!",
        "What’s your favorite type of weather? Let’s discuss meteorology!",
        "Have you ever experienced extreme weather conditions? Let’s share stories!",
        "What’s the best way to stay comfortable during hot weather? Let’s discuss tips!",
        "Do you like watching weather forecasts? Let’s discuss weather prediction!",
        "What’s your view on how weather impacts daily life? Let’s discuss!",
        "Have you ever been caught in a sudden rainstorm? Let’s share our experiences!",
        "Do you enjoy outdoor activities regardless of weather? Let’s discuss adventures!",
        "What’s the coldest temperature you’ve experienced? Let’s share weather memories!",
        "Have you ever witnessed a beautiful sunrise or sunset? Let’s discuss natural beauty!"
    ],
    "technology-related": [
        "Are you interested in technology? Let’s discuss the latest innovations.",
        "Have you tried any new gadgets lately? Let’s discuss technology!",
        "Do you have a favorite tech company? Let’s chat about technology!",
        "What’s your opinion on the future of technology? Let’s discuss trends!",
        "Are there any technological advancements that amaze you? Let’s discuss!",
        "Have you ever attended a tech conference? Let’s talk about industry insights!",
        "Do you enjoy exploring new software applications? Let’s discuss our favorites!",
        "What’s your view on the impact of technology on daily life? Let’s discuss!",
        "Are you curious about emerging tech startups? Let’s share our discoveries!",
        "Have you ever tried coding or programming? Let’s discuss our tech skills!",
        "Do you think AI will revolutionize industries? Let’s discuss the potential!"
    ],
    "history-related": [
        "Do you enjoy history? Let’s discuss your favorite historical periods.",
        "Have you read any interesting history books lately? Let’s share insights!",
        "What historical events fascinate you the most? Let’s talk about history!",
        "Do you think history repeats itself? Let’s discuss the lessons learned!",
        "Are there any historical figures you admire? Let’s discuss their impact!",
        "Have you ever visited historical landmarks? Let’s share our travel experiences!",
        "Do you enjoy exploring museums? Let’s discuss our favorite exhibits!",
        "What’s your view on how history is taught in schools? Let’s discuss!",
        "Are you interested in ancient civilizations? Let’s explore our curiosity!",
        "Have you ever watched historical documentaries? Let’s discuss our perspectives!",
        "Do you believe in preserving historical artifacts? Let’s discuss cultural heritage!"
    ],
    "science-related": [
        "Are you interested in science? Let’s discuss fascinating scientific discoveries.",
        "Have you heard about any recent scientific breakthroughs? Let’s chat!",
        "Do you have a favorite branch of science? Let’s talk about science!",
        "What scientific mysteries intrigue you the most? Let’s discuss!",
        "Are there any science experiments you’d like to try? Let’s explore ideas!",
        "Have you ever participated in citizen science projects? Let’s discuss our contributions!",
        "Do you think science fiction can predict future scientific advancements? Let’s discuss!",
        "What’s your opinion on the role of ethics in scientific research? Let’s discuss!",
        "Are you curious about space exploration? Let’s discuss the mysteries of the universe!",
        "Have you ever attended science fairs or expos? Let’s share our experiences!",
        "Do you believe in the importance of science education? Let’s discuss lifelong learning!"
    ],
    "animals-related": [
        "Are you an animal lover? Let’s discuss your favorite animals.",
        "Have you ever had a pet? Let’s talk about our furry friends!",
        "What’s the most fascinating animal fact you know? Let’s share!",
        "Do you have a favorite animal in the wild? Let’s discuss wildlife!",
        "Have you ever visited an animal sanctuary? Let’s talk about animal conservation!",
        "What’s your opinion on animal rights? Let’s discuss ethical treatment.",
        "Are there any endangered species you’re passionate about? Let’s discuss conservation efforts!",
        "Do you enjoy watching nature documentaries? Let’s discuss our favorite shows!",
        "Have you ever volunteered at an animal shelter? Let’s share our experiences!",
        "Are you interested in learning about new animal species? Let’s discuss biodiversity!",
        "What’s your view on the bond between humans and animals? Let’s discuss companionship!"
    ],
    "travel-related": [
        "Do you enjoy traveling? Let’s discuss your favorite travel destinations.",
        "Have you been on any memorable trips lately? Let’s share travel stories!",
        "What’s the most adventurous travel experience you’ve had? Let’s discuss!",
        "Do you prefer solo travel or group travel? Let’s discuss travel preferences!",
        "Have you ever traveled to a country with a different culture? Let’s discuss cultural experiences!",
        "What’s your dream travel destination? Let’s talk about bucket-list adventures!",
        "Have you ever explored off-the-beaten-path locations? Let’s share travel tips!",
        "What’s your view on sustainable travel practices? Let’s discuss responsible tourism!",
        "Do you collect souvenirs from your travels? Let’s talk about travel memories!",
        "Have you ever tried local cuisine while traveling? Let’s discuss food adventures!",
        "What’s your favorite mode of transportation while traveling? Let’s discuss travel logistics!"
    ]
}


from Body.Speech_to_Text import Speech_to_Text_Python
from Body.Advance_speak import fspeak
# Function to get a random response from a category
def get_random_response(category):
    return random.choice(responses.get(category, responses["default"]))

# Function to determine response category based on user input
def get_response(command):
    command = Speech_to_Text_Python().lower()
    # Check if input matches any specific response
    if command in responses.get("responses", {}):
        return responses["responses"][command]
    
    # Determine category based on user input
    if command in ["hello", "hi", "hey", "good morning", "good afternoon", "good evening", "howdy", "greetings", "what's up", "what's new"]:
        d = get_random_response("greetings")
        fspeak(d)
        return d
    elif command in ["bye", "see you later", "farewell", "catch you later", "take care"]:
        return get_random_response("farewells")
    elif command in ["thanks", "thank you", "thanks a lot", "thank you very much"]:
        return get_random_response("thanks")
    elif any(question in command for question in ["how", "why", "what", "when", "where"]):
        return get_random_response("questions")
    elif any(comment in command for comment in ["comment", "say", "think", "feel"]):
        return get_random_response("comments")
    elif any(word in command for word in ["joke", "funny", "laugh", "humor"]):
        return get_random_response("jokes")
    elif any(word in command for word in ["motivate", "inspire", "encourage"]):
        return get_random_response("motivational")
    elif any(word in command for word in ["advice", "suggest", "recommend"]):
        return get_random_response("advice")
    elif any(word in command for word in ["encourage", "boost", "support"]):
        return get_random_response("encouragement")
    elif any(word in command for word in ["remind", "note", "important"]):
        return get_random_response("reminders")
    elif any(word in command for word in ["sorry", "sympathize", "condolences"]):
        return get_random_response("sympathy")
    elif any(word in command for word in ["celebrate", "congratulations", "achievement"]):
        return get_random_response("celebration")
    else:
        return get_random_response("default")

# Simulated conversation loop
def conversation():
    fspeak("Start the conversation. Type 'bye', 'see you later', or 'farewell' to end.")
    while True:
        command = Speech_to_Text_Python()  
        response = get_response(command)
        fspeak(response)
        if command.lower() in ["bye", "see you later", "farewell"]:
            break

# Start the conversation
conversation()
