#Centre number: 10854
#Candidate number: 7116
#Name: Shaun Sevume

import time #This is necessary so that I can use the time.sleep function.
import re #A module that contains regular expressions and operations.
print("Welcome to the multicellular Troubeshooting program. 2.0! This new version comes with a brand new feature: Keyword identification!\n\nYou can now enter your problem and our program will do its best to identify keywords to relay help right back to you!\nThis program is still in its early stages, so solutions are limited, but we hope to expand soon!")
time.sleep(2)#This makes the program wait before executing the next line. How long it waits depends on the number specified in the brackets, which is in seconds.
print("\nBefore we begin, what is your name?")#The print function is used to output text to the user.
time.sleep(1)#See line 8
name = input("My name is: ")#This will be where the user enters their name. This variable will be re-used in the code, and not only does it avoid repetition of asking for their name constantly, it makes the program more user-friendly, addressing by their name instead of just a user number.
print("\nOkay " + name + ", this time there won't be a list of options to select from. Simply enter your problem and we'll try our best to diagnose it!\n\nSince our program is again in its early stage, we kindly ask you to keep your inputs in lower case, with no spaces at the end and no extra puncuation such as\nexclamation marks. This is so that the program runs smoothy. We also ask that you refrain from using contractions such as 'wont' or 'isnt', just for the time being\nuntil we further develop our program to understand more user inputs.\n")
time.sleep(3)#See line 8.

def nothingDefined():#This is where a function is defined, to avoid repetition in the code. This way, you simply have to call this function when needed, instead of rewriting it.
    print("\nTry and enter something that's maybe a little shorter, such as 'phone not turning on' or 'device not charging'. Remember that our program is currently limited in the words it \ncan understand.")
    return_toMenu()#Here, the return_toMenu() function is called.
    
def feedback():#See line 15.
    feedback = 0#The variable you're using in the while loop must be declared prior to the loop, or else you get an error saying that the variable hasn't been declared. For that reason, it is declared here, but given no value.

    while feedback != "y" or feedback != "n":#The while loop here means that until the answer is y or n, it will keep repeating.

        feedback = input("Did this solve your problem? (y/n) ")#This is where the user gets to input an answer. Since it only accepts the inputs y and n, it will keep asking this question until the required input is recieved.
        feedback_lower = feedback.lower()#This converts the user's input into lowercase, so that it can match the case the if statements were written in.

        if feedback_lower == "y":#This statement will be run if the variable feedback_lower has a value of "y" (given by user input).
            print("We are glad to have helped you solve your issue," + name + "!")#See line 9.
            return_toMenu()#Here, the return_toMenu() function is called. This is on line 94.

        elif feedback_lower == "n": #After the first IF statement, each subsequent one after that must be ELIF instead.
            print("We are sorry we couldn't help you solve your issue. Please try and contact your manufacturer for further advice.")#See line 9.
            return_toMenu()#See line 28.
                  
def display_problems():#See line 15.
    displaySolution = open("solutions.txt", "r")#Here it opens the txt file where the solutions are, with "r" standing for "read".
    time.sleep(1)#See line 8.
    print("\n" + displaySolution.readlines()[0])#Since it is all in one file, this specifies what lines to read, which will contain the appropriate solution.
    feedback() #Calls the feedback() function on line 19.

def battery_problems():#See line 15.
    time.sleep(1)#See line 8.
    batterySolution = open("solutions.txt", "r")#See line 36.
    print("\n" + batterySolution.readlines()[1])#See line 38.
    feedback()#See line 39.

def touchScreen_problems():#See line 15.
    time.sleep(1)#See line 8.
    touchScreenSolution = open("solutions.txt", "r")#See line 36.
    print("\n" + touchScreenSolution.readlines()[2])#See line 38.
    feedback()#See line 39.

def volume_problems():#See line 15.
    time.sleep(1)#See line 8.
    volumeSolution = open("solutions.txt", "r")#See line 36.
    print("\n" + volumeSolution.readlines()[3])#See line 38.
    feedback()#See line 39.

def calling_problems():#See line 15.
    time.sleep(1)#See line 8.
    callingSolution = open("solutions.txt", "r")#See line 36.
    print("\n" + callingSolution.readlines()[4])#Since it is all in one file, this specifies what lines to read.
    feedback()#See line 39.

def texting_problems():#See line 15.
    time.sleep(1)#See line 8.
    textingSolution = open("solutions.txt", "r")#See line 36.
    print("\n" + textingSolution.readlines()[5])#See line 38.
    feedback()#See line 39.

def internet_problems():#See line 15.
    time.sleep(1)#See line 8.
    internetSolution = open("solutions.txt", "r")#See line 36.
    print("\n" + internetSolution.readlines()[6])#See line 38.
    feedback()#See line 39.

def dim_problems():#See line 15.
    time.sleep(1)#See line 8.
    dimSolution = open("solutions.txt", "r")#See line 36.
    print("\n" + dimSolution.readlines()[7])#See line 38.
    feedback()#See line 39.

def mic_problems():#See line 15.
    time.sleep(1)#See line 8.
    micSolution = open("solutions.txt", "r")#See line 36.
    print("\n" + micSolution.readlines()[8])#See line 38.
    feedback()#See line 39.
        
def the_end():#See line 15.
    time.sleep(1)#See line 8.
    print("\nHave a nice day!")
    raise SystemExit #This terminates the program properly, so it isn't left running with nothing to display and nothing to be inputted.

def return_toMenu():#See line 15.
    time.sleep(1)#See line 8.
    return1 = 0 #Before putting a variable in a while loop, this was necessary so that it was at least defined beforehand to prevent variable errors.

    while return1 != "y" or return1 != "n":#In this while loop, it will keep asking the user to return to the main menu until a valid input is entered.

        return1 = input("\nReturn to main menu?(y/n) ")#See line 24.
        return1_lower = return1.lower()#See line 25.

        if return1_lower == "y":#See line 27
            main_menu()#Calls the main_menu() function on line 109.

        elif return1_lower == "n":#See line 31
            the_end()#Calls the the_end() function on line 89.

def main_menu():#See line 15.
    Validation = 0 #This is a counter for the loop.
    problem = input("Go ahead. What seems to be your problem? Do not enter multiple problems at once! ")#Here, the user has to input their problem. It is then assigned to the variable 'problem'.
    problem_lower = problem.lower()#See line 25.
    user_problem = problem_lower.split() #The .split function splits the words in each variable by spaces, to better identify keywords.
    numberOfWords = len(user_problem) #The len function counts how many characters are in something. 
    while Validation != 999: #As long as the counter is below 999, this loop is run.
        for i in range(numberOfWords): #'i' can represent any number. The range function specifies what range to look in, which is in this case the amount of words in the user's input.
            if user_problem[i] == "display" or user_problem[i] == "blank" or user_problem[i] == "turn" and "on" or user_problem[i] == "screen":#If any of these keywords are detected, then python will go to the appropriate function, based on what keyword was identified.
                display_problems()#Calls the display_problems() function on line 35.

            elif user_problem[i] == "charge" or user_problem[i] == "battery" or user_problem[i] == "dead" or user_problem[i] == "charging" or user_problem[i] == "die":#See line 117.
                battery_problems()#Calls the battery_problems() function on line 41.

            elif user_problem[i] == "touch" and "screen" or user_problem[i] == "touch":#See line 117.                
                touchScreen_problems()#Calls the touchScreen_problems() function on line 47.

            elif user_problem[i] == "volume" or user_problem[i] == "sound" or user_problem[i] == "speaker":#See line 117.                
                volume_problems()#Calls the volume_problems() function on line 53.

            elif user_problem[i] == "call" or user_problem[i] == "ring" or user_problem[i] == "calls":#See line 117.                
                calling_problems()#Calls the calling_problems() function on line 59.

            elif user_problem[i] == "text" or user_problem[i] == "message" or user_problem[i] == "SMS":#See line 117.                
                texting_problems()#Calls the texting_problems() function on line 65.

            elif user_problem[i] == "internet" or user_problem[i] == "connect" or user_problem[i] == "wi" and "fi"  or user_problem[i] == "web":#See line 117.                
                internet_problems()#Calls the internet_problems() function on line 71.

            elif user_problem[i] == "dim" or user_problem[i] == "bright" or user_problem[i] == "brightness":#See line 117.                
                dim_problems()#Calls the dim_problems() function on line 78.

            elif user_problem[i] == "mic" or user_problem[i] == "microphone":#See line 117.               
                mic_problems()#Calls the mic_problems() function on line 84.

        Validation +=1 #Once all the if statements are checked, it adds one to the counter and runs the loop again, this time searching for keywords one space further along.

        if Validation == 999: #This if statement is run once the for loop has run 999 times (which is very quick to a computer). By this stage, we can be sure no keywords have been defined.
            nothingDefined()#Calls the nothinDefined() function on line 15


main_menu() #This is important to starting the code. Although all the def functions have been defined by this point, none have been referenced, and so calling one here starts off the chain of def functions.
