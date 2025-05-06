import random
import re

# Chatbot identity
BOT_NAME = "Lenskart Assistant"

# Responses
responses = {
    "greeting": [
        "Hello! Welcome to Lenskart. How can I assist you today?",
        "Hi there! How can I help you with your eyewear needs?",
        "Welcome to Lenskart! What can I do for you?"
    ],
    "products": [
        "We offer eyeglasses, sunglasses, and contact lenses. Looking for anything specific?",
        "Our collection includes prescription glasses, blue light glasses, and stylish shades. Interested in any?",
        "We have computer glasses, zero power lenses, and more. Let me know what you need!"
    ],
    "track_order": [
        "Sure! Please provide your order ID (e.g., LK12345).",
        "I just need your order number to check the status. Please type it in."
    ],
    "track_order_followup": [
        "Thanks! Order ID {order_id} is on its way and should arrive in 2–3 days."
    ],
    "return_policy": [
        "We offer 14-day easy returns. The item must be unused and in original condition. Want to start a return?",
        "Most products are returnable within 14 days. Let me know if you’d like to begin the process."
    ],
    "store_locator": [
        "Sure! Please tell me your city and I’ll find the nearest store.",
        "Let me help. Which city are you in?"
    ],
    "store_locator_result": [
        "We have stores in {city}: Phoenix Mall, City Center, and Skyline Plaza. Visit anytime!"
    ],
    "offers": [
        "Right now, we’re offering *Buy 1 Get 1 Free* on select frames!",
        "Check out our latest deals on blue light glasses and power sunglasses!",
        "Students get an extra 10% off. Just show your ID in-store or apply the code STUDENT10 online!"
    ],
    "faq": [
        "Our lenses are made with high-index material and have UV protection.",
        "Yes, we provide anti-glare and scratch-resistant coatings on request.",
        "You can upload your prescription or visit the nearest store for a free eye test!"
    ],
    "help": [
        "You can ask me about products, track orders, locate stores, return policies, or available offers.",
        "Try asking things like 'Where is my order?', 'What are the offers?', or 'Return my glasses'."
    ],
    "goodbye": [
        "Thanks for visiting Lenskart! Stay stylish",
        "Glad to assist you. Have a wonderful day!",
        "Goodbye! Reach out anytime you need eyewear help."
    ],
    "fallback": [
        "Hmm, I didn't get that. Want to try asking differently?",
        "I'm a bit confused Can you clarify your question?",
        "Not sure how to help with that—maybe try 'help' to see what I can do."
    ]
}

# Keywords for intent detection
keywords = {
    "greeting": ["hello", "hi", "hey", "greetings"],
    "products": ["glasses", "sunglasses", "frames", "contact lenses", "buy", "product", "lenses"],
    "track_order": ["track", "status", "order", "delivery"],
    "return_policy": ["return", "exchange", "refund", "cancel"],
    "store_locator": ["store", "shop", "near", "location", "physical store", "city"],
    "offers": ["offer", "discount", "deal", "promo", "sale"],
    "faq": ["lens", "material", "scratch", "anti-glare", "prescription", "power", "coating", "uv"],
    "help": ["help", "support", "how", "can you", "what can"],
    "goodbye": ["bye", "goodbye", "thanks", "thank you", "exit"]
}

# Context memory
context = {
    "last_intent": None,
    "order_id": None,
    "city": None,
    "fallback_count": 0
}

def detect_intent(user_input):
    for intent, words in keywords.items():
        for word in words:
            if re.search(r'\b' + re.escape(word) + r'\b', user_input.lower()):
                return intent
    return "fallback"

def get_response(user_input):
    user_input = user_input.lower()

    # Handle store locator follow-up
    # Handle store locator follow-up
    if context["last_intent"] == "store_locator":
        known_cities = ["Mumbai", "Delhi", "Bangalore", "Hyderabad", "Pune", "Chennai", "Kolkata", "Ahmedabad"]
        for city in known_cities:
            if city.lower() in user_input:
                context["last_intent"] = None
                return random.choice(responses["store_locator_result"]).format(city=city)
        
        # If no known city found, try to extract the last word (fallback method)
        words = user_input.strip().split()
        if words:
            possible_city = words[-1].capitalize()
            context["last_intent"] = None
            return random.choice(responses["store_locator_result"]).format(city=possible_city)


    # Handle order tracking follow-up
    if context["last_intent"] == "track_order":
        match = re.search(r'(lk\d{5,})', user_input)
        if match:
            order_id = match.group(1).upper()
            context["last_intent"] = None
            return random.choice(responses["track_order_followup"]).format(order_id=order_id)

    # Detect new intent
    intent = detect_intent(user_input)
    context["last_intent"] = intent

    if intent == "fallback":
        context["fallback_count"] += 1
        if context["fallback_count"] >= 2:
            context["fallback_count"] = 0
            return random.choice(responses["help"])
        return random.choice(responses["fallback"])

    context["fallback_count"] = 0
    return random.choice(responses[intent])

# Main loop
print(f"{BOT_NAME}: Hello! I'm your Lenskart helper. Type 'exit' to end the chat.")

while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit', 'bye']:
        print(f"{BOT_NAME}: {random.choice(responses['goodbye'])}")
        break
    print(f"{BOT_NAME}: {get_response(user_input)}")













# Explanation of the Code in Detail
# This is a simple chatbot program that provides information about eyewear products, helps with tracking orders, offers details about return policies, locates stores, gives current offers, and answers FAQs related to eyewear products. The bot uses keyword matching to detect user intent and responds accordingly.

# Let's break down the code line by line:

# 1. Chatbot Identity and Responses
# python
# Copy
# Edit
# BOT_NAME = "Lenskart Assistant"
# Purpose: Defines the name of the chatbot, which is used to refer to it in conversations.

# python
# Copy
# Edit
# responses = {
#     "greeting": [
#         "Hello! Welcome to Lenskart. How can I assist you today?",
#         "Hi there! How can I help you with your eyewear needs?",
#         "Welcome to Lenskart! What can I do for you?"
#     ],
#     # Other categories like products, order tracking, return policy, etc. are similar
# }
# Purpose: Defines the different responses for each intent (e.g., greeting, products, track order, etc.). These are preset responses that the chatbot will randomly choose when a user inputs a query that matches a particular intent.

# 2. Keywords for Intent Detection
# python
# Copy
# Edit
# keywords = {
#     "greeting": ["hello", "hi", "hey", "greetings"],
#     "products": ["glasses", "sunglasses", "frames", "contact lenses", "buy", "product", "lenses"],
#     "track_order": ["track", "status", "order", "delivery"],
#     # More intents for other actions like return policy, store locator, offers, etc.
# }
# Purpose: Contains predefined keywords for each intent. When a user enters a message, the chatbot will look for these keywords to detect the user's intent (e.g., if the message contains words like "order", it will trigger the "track_order" intent).

# 3. Context Memory
# python
# Copy
# Edit
# context = {
#     "last_intent": None,
#     "order_id": None,
#     "city": None,
#     "fallback_count": 0
# }
# Purpose: Stores information about the current session. The context tracks:

# last_intent: The most recent intent detected (e.g., if the last action was a "track_order" request).

# order_id and city: Stores specific data that might be needed for follow-up questions (e.g., the order ID for tracking or city for store locator).

# fallback_count: Tracks how many times the chatbot has failed to understand a query. If there are too many failures, the bot offers more help.

# 4. Intent Detection Function
# python
# Copy
# Edit
# def detect_intent(user_input):
#     for intent, words in keywords.items():
#         for word in words:
#             if re.search(r'\b' + re.escape(word) + r'\b', user_input.lower()):
#                 return intent
#     return "fallback"
# Purpose:

# Takes the user input and checks whether it contains any of the predefined keywords for each intent.

# It loops through each intent and its associated keywords. If a keyword matches the user’s input, it returns the corresponding intent.

# re.search: This ensures that the keyword is matched as a whole word, not as part of another word (e.g., "glasses" will match "glasses", but not "sunglasses").

# If no intent is matched, it returns "fallback", indicating that the bot was unable to detect the user's intent.

# 5. Response Generation Function
# python
# Copy
# Edit
# def get_response(user_input):
#     user_input = user_input.lower()
# Purpose: Takes the user’s input, processes it, and generates an appropriate response based on the detected intent.

# python
# Copy
# Edit
#     if context["last_intent"] == "store_locator":
#         known_cities = ["Mumbai", "Delhi", "Bangalore", "Hyderabad", "Pune", "Chennai", "Kolkata", "Ahmedabad"]
#         for city in known_cities:
#             if city.lower() in user_input:
#                 context["last_intent"] = None
#                 return random.choice(responses["store_locator_result"]).format(city=city)
# Purpose: If the last intent was "store_locator", the chatbot checks if any of the known cities are mentioned in the user’s input.

# If a city is found in the input, it returns a response with the store information for that city. The format() method inserts the city name into the response.

# python
# Copy
# Edit
#     if context["last_intent"] == "track_order":
#         match = re.search(r'(lk\d{5,})', user_input)
#         if match:
#             order_id = match.group(1).upper()
#             context["last_intent"] = None
#             return random.choice(responses["track_order_followup"]).format(order_id=order_id)
# Purpose: If the last intent was "track_order", it checks if the user’s input contains an order ID (e.g., LK12345).

# The regular expression (lk\d{5,}) matches strings like "LK12345".

# If an order ID is found, it returns a response with the order status.

# python
# Copy
# Edit
#     intent = detect_intent(user_input)
#     context["last_intent"] = intent
# Purpose: If no follow-up actions are needed, the chatbot detects a new intent using detect_intent(). The detected intent is then saved in the context["last_intent"] for future reference.

# python
# Copy
# Edit
#     if intent == "fallback":
#         context["fallback_count"] += 1
#         if context["fallback_count"] >= 2:
#             context["fallback_count"] = 0
#             return random.choice(responses["help"])
#         return random.choice(responses["fallback"])
# Purpose: If the intent is "fallback" (meaning the bot couldn’t detect the user’s intent), the bot will attempt to handle the failure. It increases the fallback_count. If there are two consecutive failures, it will offer the user help (e.g., "Try asking things like 'Where is my order?'").

# python
# Copy
# Edit
#     context["fallback_count"] = 0
#     return random.choice(responses[intent])
# Purpose: If a valid intent is detected, the bot returns a response corresponding to that intent. The random.choice() ensures that the bot picks a random response from the list of possible responses for the given intent.

# 6. Main Loop
# python
# Copy
# Edit
# print(f"{BOT_NAME}: Hello! I'm your Lenskart helper. Type 'exit' to end the chat.")
# Purpose: Displays the greeting message from the chatbot when the program starts.

# python
# Copy
# Edit
# while True:
#     user_input = input("You: ")
#     if user_input.lower() in ['exit', 'quit', 'bye']:
#         print(f"{BOT_NAME}: {random.choice(responses['goodbye'])}")
#         break
#     print(f"{BOT_NAME}: {get_response(user_input)}")
# Purpose: The main loop where the bot interacts with the user.

# The bot continuously asks for user input.

# If the user types "exit", "quit", or "bye", the bot responds with a goodbye message and exits the loop.

# Otherwise, the bot processes the input and generates an appropriate response.

# Key Concepts:
# Intent Detection: The bot tries to detect the user’s intent by matching keywords from the input with predefined keywords associated with different intents (e.g., greeting, product inquiry, order tracking).

# Context Memory: The bot maintains context between interactions to handle follow-up queries (e.g., order tracking or store locator).

# Fallback Mechanism: The bot uses a fallback mechanism when it cannot understand the user’s input, providing help or asking the user to clarify.

# Random Responses: For each intent, multiple responses are available. The bot selects one randomly to make the interaction feel less robotic.

# Example Interaction:
# User: Hi
# Bot: Hello! Welcome to Lenskart. How can I assist you today?

# User: Track my order
# Bot: I just need your order number to check the status. Please type it in.

# User: LK12345
# Bot: Thanks! Order ID LK12345 is on its way and should arrive in 2–3 days.

# User: Exit
# Bot: Glad to assist you. Have a wonderful day!







# You said:
# give dry run detail


# ChatGPT said:
# Dry Run of the Code
# Let's go through a step-by-step dry run of the code with an example interaction. We'll assume the user asks a few questions, and the bot provides answers based on the defined responses and the keywords it detects.

# Setup:
# Bot Name: Lenskart Assistant

# Responses: Predefined responses for each type of query (greeting, products, track order, etc.)

# Keywords: Keywords associated with each intent (e.g., for "greeting" we have keywords like "hello", "hi", etc.)

# Context: The context dictionary keeps track of the last intent, user-provided order IDs, city information, and how many times the bot has failed to understand the input.

# Example Interaction:
# Step 1: User Starts the Chat
# Bot Output:

# text
# Copy
# Edit
# Lenskart Assistant: Hello! I'm your Lenskart helper. Type 'exit' to end the chat.
# The chatbot introduces itself and gives the user the option to exit the conversation.

# Step 2: User Greets the Bot
# User Input:

# text
# Copy
# Edit
# Hi
# Detect Intent:

# The bot receives the input "Hi".

# It checks the keywords dictionary and finds that "hi" is part of the greeting intent.

# Generate Response:

# The bot selects a random response from the greeting responses:

# text
# Copy
# Edit
# "Hello! Welcome to Lenskart. How can I assist you today?"
# Bot Output:

# text
# Copy
# Edit
# Lenskart Assistant: Hello! Welcome to Lenskart. How can I assist you today?
# The conversation continues with the bot greeting the user and asking how it can help.

# Step 3: User Inquires About Products
# User Input:

# text
# Copy
# Edit
# What products do you sell?
# Detect Intent:

# The bot receives the input "What products do you sell?".

# It checks the keywords dictionary and finds that the word "products" is part of the products intent.

# Generate Response:

# The bot selects a random response from the products responses:

# text
# Copy
# Edit
# "We offer eyeglasses, sunglasses, and contact lenses. Looking for anything specific?"
# Bot Output:

# text
# Copy
# Edit
# Lenskart Assistant: We offer eyeglasses, sunglasses, and contact lenses. Looking for anything specific?
# The bot responds with details about the products offered and asks if the user is looking for something specific.

# Step 4: User Asks About Tracking Their Order
# User Input:

# text
# Copy
# Edit
# Can I track my order?
# Detect Intent:

# The bot receives the input "Can I track my order?".

# It checks the keywords dictionary and finds that "track" and "order" are part of the track_order intent.

# Generate Response:

# The bot responds by asking the user for their order ID:

# text
# Copy
# Edit
# "Sure! Please provide your order ID (e.g., LK12345)."
# Bot Output:

# text
# Copy
# Edit
# Lenskart Assistant: Sure! Please provide your order ID (e.g., LK12345).
# The bot is now waiting for the user to provide their order ID.

# Step 5: User Provides Order ID
# User Input:

# text
# Copy
# Edit
# LK12345
# Track Order Intent:

# The bot receives the input "LK12345".

# It matches the regular expression r'(lk\d{5,})', which looks for order IDs like "LK12345".

# Generate Response:

# The bot then extracts the order ID and checks if it’s a valid order.

# The bot selects a random response from the track_order_followup responses, including the order ID:

# text
# Copy
# Edit
# "Thanks! Order ID LK12345 is on its way and should arrive in 2–3 days."
# Bot Output:

# text
# Copy
# Edit
# Lenskart Assistant: Thanks! Order ID LK12345 is on its way and should arrive in 2–3 days.
# The bot informs the user about the status of their order.

# Step 6: User Asks About Offers
# User Input:

# text
# Copy
# Edit
# What offers do you have right now?
# Detect Intent:

# The bot receives the input "What offers do you have right now?".

# It checks the keywords dictionary and finds that "offer" is part of the offers intent.

# Generate Response:

# The bot selects a random response from the offers responses:

# text
# Copy
# Edit
# "Right now, we’re offering *Buy 1 Get 1 Free* on select frames!"
# Bot Output:

# text
# Copy
# Edit
# Lenskart Assistant: Right now, we’re offering *Buy 1 Get 1 Free* on select frames!
# The bot informs the user about a current offer.

# Step 7: User Says Goodbye
# User Input:

# text
# Copy
# Edit
# Bye
# Detect Intent:

# The bot receives the input "Bye".

# It checks the keywords dictionary and finds that "bye" is part of the goodbye intent.

# Generate Response:

# The bot selects a random response from the goodbye responses:

# text
# Copy
# Edit
# "Thanks for visiting Lenskart! Stay stylish"
# Bot Output:

# text
# Copy
# Edit
# Lenskart Assistant: Thanks for visiting Lenskart! Stay stylish
# The bot bids farewell and ends the conversation.

# Key Points of the Dry Run:
# Intent Detection:

# The bot analyzes the user’s input and matches keywords to identify the intent (e.g., greeting, order tracking, offers, etc.).

# The function detect_intent is responsible for this by looping through predefined keywords.

# Context Handling:

# If the user asks for order tracking or store locator, the bot stores the context (like order ID or city) to handle follow-up questions.

# Response Selection:

# After detecting the intent, the bot randomly selects a response from the predefined list of responses related to the intent.

# Fallback Mechanism:

# If the bot can't identify the intent based on keywords (e.g., the user asks something unclear), it falls back to the "fallback" response, encouraging the user to rephrase their question.

# If there are multiple fallback responses, the bot offers additional help after a couple of consecutive failures.

# Session Continuity:

# The bot tracks the last intent using the context dictionary, which helps it provide follow-up responses when needed (e.g., after asking for an order ID or city).

# Exit Condition:

# If the user types "exit", "quit", or "bye", the bot says goodbye and ends the conversation.

# Conclusion:
# In this dry run, we can see how the chatbot processes input, identifies intent, tracks context, and responds appropriately using predefined responses. It also handles follow-up queries and provides useful fallback responses when necessary. The flow of the conversation is managed through the context and intent detection, ensuring smooth interactions with the user.




# ✅ Example Input & Output
# 1. Greeting
# Input: Hi

# Output: Hello! Welcome to Lenskart. How can I assist you today?

# 2. Ask about products
# Input: What kind of glasses do you have?

# Output: We offer eyeglasses, sunglasses, and contact lenses. Looking for anything specific?

# 3. Track an order
# Input: Track my order

# Output: Sure! Please provide your order ID (e.g., LK12345).

# Follow-up Input: lk98765

# Follow-up Output: Thanks! Order ID LK98765 is on its way and should arrive in 2–3 days.

# 4. Return policy
# Input: Can I return my glasses?

# Output: We offer 14-day easy returns. The item must be unused and in original condition. Want to start a return?

# 5. Store locator
# Input: Is there a store in Bangalore?

# Output: We have stores in Bangalore: Phoenix Mall, City Center, and Skyline Plaza. Visit anytime!

# 6. Offers
# Input: Any discount available?

# Output: Right now, we’re offering *Buy 1 Get 1 Free* on select frames!

# 7. FAQ
# Input: Do lenses have UV protection?

# Output: Our lenses are made with high-index material and have UV protection.

# 8. Exit
# Input: bye

# Output: Goodbye! Reach out anytime you need eyewear help.

# 🎓 Viva Questions & Answers (Short)
# Q: What is the purpose of this chatbot?
# A: To assist users with Lenskart services like product info, order tracking, returns, and store locations.

# Q: How is user intent identified?
# A: Using keyword matching with regular expressions via the detect_intent() function.

# Q: How does the chatbot handle follow-up questions like order tracking?
# A: It stores the previous intent and looks for specific inputs like order ID if the last intent was track_order.

# Q: What happens if user input doesn't match any keyword?
# A: The chatbot replies with a fallback message. After two such cases, it suggests help.

# Q: How does the bot customize responses like city or order ID?
# A: Using .format() with placeholders like {city} or {order_id} to insert dynamic values.

# Q: What is the role of the context dictionary?
# A: It remembers the last intent and other details (e.g., fallback count, city, order ID) for smooth conversation flow.

# Would you like a short flowchart or diagram for this chatbot system?








