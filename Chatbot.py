import nltk
from nltk.chat.util import Chat, reflections

# Define a set of pairs for the chatbot
pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I assist you today?", "Hi there! How can I help?", "Hey! What's on your mind?"]
    ],
    [
        r"what is your name\??",
        ["I'm a chatbot. You can call me ChatBuddy!", "I don't have a name, but you can call me ChatBot."]
    ],
    [
        r"how are you\??",
        ["I'm just a bunch of code, but I'm here to assist you!", "I'm good! Ready to help you."]
    ],
    [
        r"what can you do\??",
        ["I can have simple conversations with you. Try asking me something!", "I'm here to chat and assist with your questions."]
    ],
    [
        r"tell me a joke",
        ["Why don’t skeletons fight each other? They don’t have the guts!", "Why don’t scientists trust atoms? Because they make up everything!"]
    ],
    [
        r"bye|exit|quit",
        ["Goodbye! Have a great day!", "See you later! Take care!", "Bye! It was nice talking to you."]
    ],
    [
        r"(.*)",
        ["I'm not sure how to respond to that. Can you try rephrasing?", "Interesting! Tell me more.", "I'm here to listen."]
    ]
]

# Initialize the chatbot
def chatbot():
    print("ChatBot: Hello! Type 'bye' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

# Main function
if __name__ == "__main__":
    chatbot()
