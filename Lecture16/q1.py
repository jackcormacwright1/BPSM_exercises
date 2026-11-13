#!/bin/python3

##############################################################################################

#exercise 1

#With the aid of a function and a dictionary, write an interactive Python programme/script 
#that will ask the user the following questions

#What's your name?
#How old are you?
#What is your favourite colour?
#Do you like Python?
#The world is flat: True or False?

#and then, based on their answers, make some comments back to them 
#(this doesn't have to be at all serious, it's the methods used that we are trying out here....!)

############################################################################################


def get_answers(questions):
    answers = {}

    for key, question in questions.items():
        answer = input(question + " ").strip()
        answers[key] = answer

    return answers

questions = {
    "name": "What's your name?",
    "age": "How old are you?",
    "colour": "What is your favourite colour?",
    "python": "Do you like Python?",
    "flat_earth": "The world is flat: True or False?"
}

answers = get_answers(questions)

print()
print(f"hello {answers['name']}!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print(f"you are {answers['age']}????? sooooo old!!!!!!!! ewwwwwwwwwww")
print(f"{answers['colour']} is the worst colour i bet ur ugly!!!!!!!!!!!!!!!!!")

if answers["python"].lower() == "yes":
    print("i bet u like python u nerd!!!!!!!!!!!!!!!!!")
elif answers["python"].lower() == "no":
    print("WRONG! i dont like u either nerd!!!!!!!!!!!!!!!!!!")
else:
    print("learn how to answer a question properly nerd!!!!!!!")

if answers["flat_earth"].lower() == "false":
    print("water always finds its level explain that weatherboy!!!!!!!")
elif answers["flat_earth"].lower() == "true":
    print("meet u over the ice wall brotherrr!!!!!!!!!!!!!")
else:
    print("its true or false numpty...")









