import random
from datetime import datetime
import pyjokes
def main():
    greetings = [
        "Hello!",
        "Hi there!",
        "Hey!",
        "Greetings!",
        "Howdy!",
        "What's up?",
        "Yo!",
        "Hiya!",
        "Nice to see you!",
        "Welcome!"
    ]
    farewells = [
        "Goodbye!",
        "See you later!",
        "Take care!",
        "Catch you soon!",
        "Farewell!",
        "Bye for now!",
        "Until next time!",
        "Peace out!",
        "Later, alligator!",
        "May the force be with you!"
    ]
    ends = ["exit", "quit", "bye", "terminate", "see ya", "later", "no"]
    greet = random.choice(greetings)
    farewell = random.choice(farewells)

    print(greet)

    name = input("What is your name? ").strip().lower()
    if not name:
        name = "mysterious stranger"

    request = input(f"{greet} {name.title()}. What can I do for you? ").strip().lower()
    response = handle_request(request)
    print(response)

    loop = True
    while loop:
        request = input("Is there anything else I can do for you? ")
        if request in ends:
            loop = False
            break
        response = handle_request(request)
        print(response)

    print(farewell)

def handle_request(request):
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%H:%M:%S")
    joke_requests = [
    "tell me a joke",
    "say something funny",
    "make me laugh",
    "got any jokes?",
    "cheer me up",
    "funny please",
    "show me a joke",
    "give me a joke",
    "crack a joke",
    "laugh time"
]
    time_requests = [
    "what's the time",
    "tell me the time",
    "show me the time",
    "current time please",
    "time right now",
    "clock",
    "give me the time",
    "what time is it",
    "what’s the current time",
    "can you tell me the time"
]
    my_capacity = ["what can you do?", "what do you do?", "what do you have?"]
    if request in my_capacity:
        return "I can tell jokes and I can tell time"
    elif request in joke_requests:
        return pyjokes.get_joke()
    elif request in time_requests:
        return current_time
    else:
        return "Sorry, I dont understand. All I can do now is tell joke and tell time untill my stupid programmer do something about it"

if __name__ == "__main__":
    main()