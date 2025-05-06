# Assignment-B5 (Chatbot)
import datetime

def restaurant_chatbot():
    print("Welcome to the Vedant's Restaurant!")
    print("You can ask me about the menu, cost, contact details or reservations!")
    
    while True:
        user_input = input("\nYou: ").lower()
        
        if "menu" in user_input:
            print("Chatbot: Our menu includes pasta, pizza, salads, and desserts.")
            user_input1 = input("\nYour item: ").lower()
            if "pasta" in user_input1:
                print("you have ordered pasta")

        
        elif "cost" in user_input or "price" in user_input or "how much" in user_input:
            print("Chatbot: The average cost per person is around $20.")
        
        elif "contact" in user_input or "phone" in user_input:
            print("Chatbot: You can contact us at +91-1234567890")
        
        elif "reservation" in user_input or "book" in user_input:
            print("Chatbot: To make a reservation, please call us at +91-1234567890 or visit our website at https://k-rest.io")
        
        elif "hours" in user_input:
            print("Chatbot: We are open from 11 AM to 10 PM, Monday to Sunday.")
        
        elif "date" in user_input or "time" in user_input:
            now = datetime.datetime.now()
            print(f"Chatbot: Today's date and time is {now.strftime('%Y-%m-%d %H:%M:%S')}.")
        
        elif "how are you" in user_input or "how's it going" in user_input or "sup" in user_input:
            print("Chatbot: I'm just a bot, but I'm here to help you! How can I assist you today?")
        
        elif "meow" in user_input:
            print("Meow meow meow!")

        elif "exit" in user_input or "quit" in user_input:
            print("Chatbot: Thank you for chatting with us! Have a great day!")
            break
        
        else:
            print("Chatbot: I'm sorry, I didn't understand that. Can you ask something else?")

restaurant_chatbot()



# Code Explanation (Line-by-Line):
# import datetime:

# Imports the datetime module, which is used to work with date and time.

# def restaurant_chatbot()::

# Defines a function restaurant_chatbot() to handle the chatbot interactions.

# print("Welcome to the Vedant's Restaurant!"):

# Displays a welcome message to the user when the chatbot starts.

# print("You can ask me about the menu, cost, contact details or reservations!"):

# Informs the user about the topics they can ask the chatbot (menu, cost, contact, reservation).

# while True::

# Starts an infinite loop to keep the chatbot running until the user exits.

# user_input = input("\nYou: ").lower():

# Takes input from the user and converts it to lowercase for easier comparison.

# if "menu" in user_input::

# If the user's input contains the word "menu", the chatbot responds with the menu options.

# print("Chatbot: Our menu includes pasta, pizza, salads, and desserts."):

# Displays the menu items available in the restaurant.

# user_input1 = input("\nYour item: ").lower():

# Asks the user to specify the item they want to order and converts it to lowercase.

# if "pasta" in user_input1::

# If the user wants pasta, the chatbot confirms the order.

# print("you have ordered pasta"):

# Displays a confirmation message for the pasta order.

# elif "cost" in user_input or "price" in user_input or "how much" in user_input::

# If the user asks about the cost or price, the chatbot provides information about the average cost.

# print("Chatbot: The average cost per person is around $20."):

# Provides the cost information when the user asks about pricing.

# elif "contact" in user_input or "phone" in user_input::

# If the user asks for contact information, the chatbot responds with the restaurant's phone number.

# print("Chatbot: You can contact us at +91-1234567890"):

# Displays the restaurant's phone number.

# elif "reservation" in user_input or "book" in user_input::

# If the user asks about reservations, the chatbot provides instructions on how to make one.

# print("Chatbot: To make a reservation, please call us at +91-1234567890 or visit our website at https://k-rest.io"):

# Provides the reservation details with contact and website information.

# elif "hours" in user_input::

# If the user asks about opening hours, the chatbot responds with the restaurant's working hours.

# print("Chatbot: We are open from 11 AM to 10 PM, Monday to Sunday."):

# Displays the operating hours of the restaurant.

# elif "date" in user_input or "time" in user_input::

# If the user asks for the current date or time, the chatbot will provide that information.

# now = datetime.datetime.now():

# Fetches the current date and time using the datetime module.

# print(f"Chatbot: Today's date and time is {now.strftime('%Y-%m-%d %H:%M:%S')}."):

# Displays the current date and time in a readable format.

# elif "how are you" in user_input or "how's it going" in user_input or "sup" in user_input::

# If the user asks how the chatbot is doing, it replies with a friendly message.

# print("Chatbot: I'm just a bot, but I'm here to help you! How can I assist you today?"):

# The chatbot responds to the user in a friendly manner, encouraging further interaction.

# elif "meow" in user_input::

# If the user types "meow," the chatbot responds with a playful "Meow meow meow!"

# elif "exit" in user_input or "quit" in user_input::

# If the user wants to exit the chatbot, they can type "exit" or "quit."

# print("Chatbot: Thank you for chatting with us! Have a great day!"):

# The chatbot thanks the user and ends the conversation when they choose to exit.

# break:

# Exits the while loop, effectively ending the chatbot session.

# else::

# If the chatbot doesn't understand the user's input, it will ask for clarification.

# print("Chatbot: I'm sorry, I didn't understand that. Can you ask something else?"):

# The chatbot informs the user that it didn't understand the request.

# Example Input and Output
# Input 1:
# makefile
# Copy
# Edit
# You: menu
# Output 1:
# yaml
# Copy
# Edit
# Chatbot: Our menu includes pasta, pizza, salads, and desserts.

# Your item: pasta
# you have ordered pasta
# Input 2:
# makefile
# Copy
# Edit
# You: cost
# Output 2:
# pgsql
# Copy
# Edit
# Chatbot: The average cost per person is around $20.
# Input 3:
# makefile
# Copy
# Edit
# You: contact
# Output 3:
# makefile
# Copy
# Edit
# Chatbot: You can contact us at +91-1234567890
# Input 4:
# makefile
# Copy
# Edit
# You: reservation
# Output 4:
# go
# Copy
# Edit
# Chatbot: To make a reservation, please call us at +91-1234567890 or visit our website at https://k-rest.io
# Input 5:
# makefile
# Copy
# Edit
# You: how are you
# Output 5:
# vbnet
# Copy
# Edit
# Chatbot: I'm just a bot, but I'm here to help you! How can I assist you today?
# Input 6:
# makefile
# Copy
# Edit
# You: meow
# Output 6:
# nginx
# Copy
# Edit
# Meow meow meow!
# Input 7:
# vbnet
# Copy
# Edit
# You: exit
# Output 7:
# sql
# Copy
# Edit
# Chatbot: Thank you for chatting with us! Have a great day!
# Viva Questions and Answers:
# What does the restaurant_chatbot() function do?

# It simulates a chatbot for a restaurant, answering questions about the menu, cost, contact details, reservation process, hours, and more.

# How does the chatbot handle user input?

# It continuously listens for user input and processes it using if and elif conditions to match specific queries like "menu," "cost," "reservation," etc.

# What happens if the chatbot doesn't understand the user input?

# It replies with "I'm sorry, I didn't understand that. Can you ask something else?" and waits for a new input.

# What is the purpose of using datetime.datetime.now() in the code?

# It fetches the current date and time to provide real-time information when the user asks for the date or time.

# What would happen if the user types "exit" or "quit"?

# The chatbot will thank the user for chatting and then exit the conversation by breaking out of the while loop.

# How can you extend this chatbot to handle more queries?

# You can add more elif conditions to handle additional queries, such as "special offers," "location," or "reviews."

# What type of feedback does the chatbot give if the user asks for the menu?

# It provides a list of available items (pasta, pizza, salads, and desserts) and asks for further details about the item.

# How would you improve the chatbot's responses to be more dynamic?

# You can use machine learning techniques to analyze user input better and respond more intelligently, or integrate an API for more detailed responses.