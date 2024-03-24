import datetime

#print("The print() command is actually a function! The parenthese are clue.")

def greet():
    # Get the current time
    dt = datetime.datetime.now()
    if dt.hour <= 11 :
        greeting = "morning"
    elif dt.hour <= 17:
        greeting = "afternoon"
    else :
        greeting = "night"
    
    print("Hello, good " + greeting + ".")

greet()