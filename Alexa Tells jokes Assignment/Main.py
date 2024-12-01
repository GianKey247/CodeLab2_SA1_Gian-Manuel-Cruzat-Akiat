import random
f = open(r"D:\Codes\Y2 CC\Code lab 2\Codes\Alexa Tells jokes\randomJokes.txt", "r")
jokes=f.readlines()

alexa_Prompt = input("").lower()
while alexa_Prompt != "quit":
    if alexa_Prompt == "alexa tell me a joke": 
        random.shuffle(jokes)
        random_joke=random.choice(jokes)
        joke_Split=random_joke.split("?")
        joke_Setup = joke_Split[0]+"?"
        joke_Punchline = joke_Split[1]

        print(joke_Setup)
        user_Input = input("")
        print(joke_Punchline)
    
    alexa_Prompt = input("").lower()

