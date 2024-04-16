import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    ['hi|hey|hello', ['Hello!', 'Hey there!', 'Hi!']],
    ['how are you?', ['I am doing well, thank you!', 'I\'m good, thanks for asking. How about you?']],
    ['(what is your name?|who are you?)', ['I am a chatbot created using NLTK.', 'You can call me Chatbot.']],
    ['(what can you do?|what are your capabilities?)', ['I can have conversations with you and provide information.']],
    ['(quit|exit)', ['Bye!', 'Goodbye!', 'See you later!']],
    ['(.*)', ["I'm not sure I understand. Could you please rephrase that?"]]
]

# Create a Chatbot
chatbot = Chat(pairs, reflections)

# Start conversation
print("Welcome to the Chatbot. Type 'quit' to end the conversation.")
while True:
    user_input = input("You: ")
    response = chatbot.respond(user_input)
    print("Chatbot:", response)
    if user_input.lower() == 'quit':
        break
