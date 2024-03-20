import nltk
from nltk.chat.util import Chat, reflections

pairs = [
[
        r"my name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ], 
    [
        r"what is your name ?",
        ["I am a bot created by Skynet going by the name Mini_Terminator_2001",]
    ],
    [
        r"how are you ?",
        ["I'm doing good. How about you ?",]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind",]
    ],
    [
        r"I am fine",
        ["Great to hear that, How can I help you?",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that","How can I help you?:)",]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program dude. Seriously you are asking me this?",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
    ],
    [
        r"(.*) created ?",
        ["Skynet created me.",]
    ],
    [
        r"(.*) (location|city) ?",
        ['I am currently living in your pc.',]
    ],
    [
        r"how is weather in (.*)?",
        ["Weather in %1 is awesome like always","Too hot man here in %1","Too cold man here in %1","Never even heard about %1"]
    ],
    [
        r"i work in (.*)?",
        ["%1 is an amazing company, I have heard about it.",]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain since last week here in %2","Damn its raining too much here in %2"]
    ],
    [
        r"how (.*) health(.*)",
        ["I'm a computer program, so I'm always healthy ",]
    ],
    [
        r"(.*) (sports|game) ?",
        ["I'm a very big fan of Football",]
    ],
    [
        r"who (.*) sportsperson ?",
        ["Kevin De Bruyne","Andres Iniesta","Lionel Messi"]
    ],
    [
        r"who (.*) (moviestar|actor)?",
        ["Brad Pitt"]
    ],
    [
        r"i am looking to learn data science (.*)?",
        ["Andrej Karpathy has many great vidoes on YouTube with step by step explanation along with code, you can explore"]
    ],
    [
        r"what's (.*) movie?",
        ["Interstellar", "Terminator"]
    ]
]

chatbot = Chat(pairs, reflections)

def chat():
    print("Hello! I'm Chatbot. How can I assist you today?")
    print("Enter 'quit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Chatbot: Bye! Take care.")
            break
        else:
            response = chatbot.respond(user_input)
            print("Chatbot:", response)

if __name__ == "__main__":
    nltk.download('punkt')
    chat()
