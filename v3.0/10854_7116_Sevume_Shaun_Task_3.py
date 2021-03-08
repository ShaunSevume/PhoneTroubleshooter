#Centre number: 10854
#Candidate number: 7116
#Name: Shaun Sevume

import time #This is necessary so that I can use the time.sleep function.
import re #Allows the code to open, read and write to txt files.
import random #Necessary for the .randint function to work. It generates a random number.
from datetime import datetime #Date and time is imported so that it can be recorded with the user's details, should they fail to find the solution.
print("Welcome to the multicellular Troubeshooting program version 3.0! In addition to version 2.0's feature of identifying keywords, we can now identify your phone model to tailor \nresults to it, as well as giving you a refrerence number for a technician if we are still unable to solve your problem! Please bear in mind that we only support iPhones, Samsungs and Sonys at the moment.")
time.sleep(2) #This makes the program wait before executing the next line. How long it waits depends on the number specified in the brackets, which is in seconds.
print("\nIn order to make this work, we're going to need a few details from you.")#The PRINT function outputs whatever is in the brackets. This is the text the user would see.
time.sleep(1)#See line 10.
    
def unresolved(): #This is where a function is defined, to avoid repetition in the code. This way, you simply have to call this function when needed, instead of rewriting it.
    record = open('unresolved cases.txt','a')#A variable is declared here and assigned to the function that opens the unresolved cases.txt file.
    record.write("\nName " + name)#.write is added to the declared variable (record), which tells python to write something in the txt file, specified in the brackets.
    record.write('\nEmail: ' + email)#(Following up from the previous point) For example, here, the code is told to write "Email: " plus whatever the user entered as their email.
    if "iphone" in make_lower:#IF statements are used here to decide whether to write iphone, samsung or sony in the file. The IN function is used to identify keywords in the variable make_lower.        
        record.write('\nDevice: iPhone '+ model)#See line 16.
    elif "samsung" in make_lower:#After the first IF statement, each subsequent one after that must be ELIF (Else if) instead, as an alternative.
        record.write('\nDevice: Samsung '+ model)#See line 16.
    elif "sony" in make_lower:#See line 20.
        record.write('\nDevice: Sony '+ model)#See line 16.        
    date_time = datetime.now() #The function datetime.now() retrieves the current date and time. This is then assigned to a variable.
    date_time = str(date_time) #Since the date and time comes in integer form, it must first be converted to a string before it can be written in the txt file
    record.write('\nDate + Time: ' + date_time) #After converting date and time to a string, it can be recorded.
    record.write('\nUser Problem: ' + problem) #Here, the problem the user had is recorded. This is what they inputted when they got asked what their problem was.
    case = random.randint(0,999) #The .randint function generates a random number, with a range you can specify in the brackets. The generated number is assigned to the variable called case.
    case = str(case) #Like with the date and time, it comes in integer form by default, so must be changed into string form to be written.
    record.write('\nCase No: ' + case)#Since the random integer is now in string format, it can be recorded in the txt file.
    record.close() #After all the details have been recorded, the txt file gets closed with the .close() function.
    print("\nWe are sorry we couldn't help you solve your issue. We have saved your details to be looked at by a technician. Your case number is " + case + ".")#Outputs an apology message and the user's case number.
    return_toMenu() #Here, a fuction is called, which is in another part of the code. 

def nothing_defined():#See line 14.
    print("\nRemember, we currently only support iPhone, Sony and Samsung.")#See line 11.
    return_toMenu2() #See line 33.
    
def nothing_defined2():#See line 14.
    print("\nSorry, but we were unable to identify any keywords. Please note that we only have a limited amount of solutions right now, so we can only solve so many \nproblems.")
    return_toMenu()#See line 33.
    
def feedback():#See line 14.
    feedback = 0 #The variable you're using in the while loop must be declared prior to the loop, or else you get an error saying that the variable hasn't been declared. For that reason, it is declared here, but given no value.

    while feedback != "y" or feedback != "n": #The while loop here means that until the answer is y or n, it will keep repeating.

        feedback = input("\nDid this solve your problem? (y/n) ")#This is the question that will be repeated until the while loop is broken. In this case, it has to become false.
        feedback_lower = feedback.lower()#See line 33.
        
        if feedback_lower == "y":#See line 18
            print("\nWe are glad to have helped you solve your issue," + name + "!")#See line 11.
            return_toMenu()#See line 33.

        elif feedback_lower == "n": #See line 20.
            unresolved()#See line 33.
                  
def display_problems():#See line 14.
    if "iphone" in make_lower:#See line 18
        iphone_displaySolution = open("iphone.txt", "r") #Here it opens the txt file where the solutions are, but is only asked to read it this time.
        time.sleep(1)#See line 10.
        print("\n" + iphone_displaySolution.readlines()[0]) #Since it is all in one file, this specifies what lines to read, which will contain the appropriate solution.
        feedback() #See line 33.

    elif "samsung" in make_lower:#See line 20.
        samsung_displaySolution = open("samsung.txt", "r")#See line 60.
        time.sleep(1)#See line 10.
        print("\n" + samsung_displaySolution.readlines()[0]) #The .readlines() function makes my code more efficient because I only have to use 1 text file for all the solutions of a model instead of seperate ones.
        feedback()#See line 33.

    elif "sony" in make_lower:#See line 20.
        sony_displaySolution = open("sony.txt", "r")#See line 60.
        time.sleep(1)#See line 10.
        print("\n" + sony_displaySolution.readlines()[0])#See line 68
        feedback()#See line 33.

def battery_problems():#See line 14.
    if "iphone" in make_lower:#See line 18
        iphone_batterySolution = open("iphone.txt", "r")#See line 60.
        time.sleep(1)#See line 10.
        print("\n" + iphone_batterySolution.readlines()[1])#See line 68
        feedback()#See line 33.

    elif "samsung" in make_lower:#See line 20.
        samsung_batterySolution = open("samsung.txt", "r")#See line 60.
        time.sleep(1)#See line 10.
        print("\n" + samsung_batterySolution.readlines()[1])#See line 68
        feedback()#See line 33.

    elif "sony" in make_lower:#See line 20.
        sony_batterySolution = open("sony.txt", "r")#See line 60.
        time.sleep(1)#See line 10.
        print("\n" + sony_batterySolution.readlines()[1])#See line 68
        feedback()#See line 33.

def touchScreen_problems():#See line 14.
    if "iphone" in make_lower:#See line 18
        iphone_touchScreenSolution = open("iphone.txt", "r")#See line 60.
        time.sleep(1)#See line 10.
        print("\n" + iphone_touchScreenSolution.readlines()[2])#See line 68
        feedback()#See line 33.

    elif "samsung" in make_lower:#See line 20.
        samsung_touchScreenSolution = open("samsung.txt", "r")#See line 60.
        time.sleep(1)#See line 10.
        print("\n" + samsung_touchScreenSolution.readlines()[2])#See line 68
        feedback()#See line 33.

    elif "sony" in make_lower:#See line 20.
        sony_touchScreenSolution = open("sony.txt", "r")#See line 60.
        time.sleep(1)#See line 10.
        print("\n" + sony_touchScreenSolution.readlines()[2])#See line 68
        feedback()#See line 33.

def dim_problems():#See line 14.
    if "iphone" in make_lower:#See line 18
        iphone_dimSolution = open("iphone.txt", "r")#See line 60.
        time.sleep(1)#See line 10.
        print("\n" + iphone_dimSolution.readlines()[3])#See line 68
        feedback()#See line 33.

    elif "samsung" in make_lower:#See line 20.
        samsung_dimSolution = open("samsung.txt", "r")#See line 60.
        time.sleep(1)#See line 10.
        print("\n" + samsung_dimSolution.readlines()[3])#See line 68
        feedback()#See line 33.

    elif "sony" in make_lower:#See line 20.
        sony_dimSolution = open("sony.txt", "r")#See line 60.
        time.sleep(1)#See line 10.
        print("\n" + sony_dimSolution.readlines()[3])#See line 68
        feedback()

def volume_problems():#See line 14.
    if "iphone" in make_lower:#See line 18
        iphone_volumeSolution = open("iphone.txt", "r")#See line 60.
        time.sleep(1)#See line 10.
        print("\n" + iphone_volumeSolution.readlines()[4])#See line 68
        feedback()#See line 33.

    elif "samsung" in make_lower:#See line 20.
        samsung_volumeSolution = open("samsung.txt", "r")#See line 60.
        time.sleep(1)#See line 10.
        print("\n" + samsung_volumeSolution.readlines()[4])#See line 68
        feedback()#See line 33.

    elif "sony" in make_lower:#See line 20.
        sony_volumeSolution = open("sony.txt", "r")#See line 60.
        time.sleep(1)#See line 10.
        print("\n" + sony_volumeSolution.readlines()[4])#See line 68
        feedback()#See line 33.

def the_end():#See line 14.
    time.sleep(1)#See line 10.
    print("\nHave a nice day!")#See line 11.
    raise SystemExit #This terminates the program properly, so it isn't left running with nothing to display and nothing to be inputted.

def return_toMenu():#See line 14.
    time.sleep(1)#See line 10.
    return1 = 0 #Before putting a variable in a while loop, this was necessary so that it was at least defined beforehand to prevent variable errors.

    while return1 != "y" or return1 != "n":#See line 46

        return1 = input("\nReturn to main menu?(y/n) ") #The input function means that the program will allow the user to input a response, which the program will 'react' to.
        return1_lower = return1.lower()
        
        if return1_lower == "y":#See line 18
            main()#See line 33.

        elif return1_lower == "n":#See line 20.
            the_end()#See line 33.

def return_toMenu2():#See line 14.
    time.sleep(1)#See line 10.
    return1 = 0#See line 160.
    
    while return1 != "y" or return1 != "n":#See line 46

        return1 = input("\nWould you like to input another phone make?(y/n) ")#See line 48.
        return1_lower = return1.lower()#See line 33.

        if return1_lower == "y":#See line 18
            phone_make()#See line 33.

        elif return1_lower == "n":#See line 20.
            device_details()#See line 33.
def main():#See line 14.
    Validation = 0 #This is a counter for the loop
    problem = input("\nWhat is the problem with your device? ")
    global problem #Here, the variable is made global, meaning it can be used elsewhere in the code. However, variables such as problem_lower are local variables, because they haven't been declared as global.
    problem_lower = problem.lower() #The .lower function converts the user's input into lowercase to match the case of the code. It is then assigned to a new variabke
    user_problem = problem_lower.split() #The .split function splits the words in each variable by spaces, to better identify keywords.
    numberOfWords = len(user_problem) #The len function counts how many characters are in something. 
    while Validation != 999: #As long as the counter is below 999, this loop is run.
        for i in range(numberOfWords): #'i' can represent any number. The range function specifies what range to look in, which is in this case the amount of words in the user's input.
            if user_problem[i] == "display" or user_problem[i] == "blank" or user_problem[i] == "turn" and "on" or user_problem[i] == "screen": #If any of the keywords are found, it will go to the appropriate function. Any keywords found in this line for example will go to the display problems function.
                display_problems()#See line 33.

            elif user_problem[i] == "charge" or user_problem[i] == "battery" or user_problem[i] == "dead" or user_problem[i] == "charging" or user_problem[i] == "die":#See line 20.
                battery_problems()#See line 33.

            elif user_problem[i] == "touch" and "screen" or user_problem[i] == "touch":#See line 20.                
                touchScreen_problems()#See line 33.

            elif user_problem[i] == "dim" or user_problem[i] == "bright" or user_problem[i] == "brightness" or user_problem[i] == "dark":#See line 20.               
                dim_problems()#See line 33.
                
            elif user_problem[i] == "volume" or user_problem[i] == "sound" or user_problem[i] == "speaker":#See line 20.                
                volume_problems()#See line 33.
       
        Validation +=1 #Once all the if statements are checked, it adds one to the counter and runs the loop again, this time searching for keywords one space further along.

        if Validation == 999: #This if statement is run once the for loop has run 999 times (which is very quick to a computer). By this stage, we can be sure no keywords have been defined/
            nothing_defined2()#See line 33.
        
def sony():#See line 14.
    confirmation = 0#See line 160.
    
    while confirmation != "y" or confirmation != "n":#See line 46
        
        model = input("\nWhich model of Sony is it? (e.g Xperia Z3, Xperia M4) " )#See line 48.
        global model#See line 190.
        confirmation = input("Sony " + model + ",correct? (y/n) ")#See line 48.
        confirmation_lower = confirmation.lower()#See line 33.

        if confirmation_lower == "y":#See line 18
            main()#See line 33.
            break #The break function is another way to stop a while loop. It tells python to 'break' (out of) the loop.
        
        elif confirmation_lower == "n":#See line 20.
            sony()#See line 33.
            break#See line 228.
        
def samsung():#See line 14.
    confirmation = 0#See line 160.
    
    while confirmation != "y" or confirmation != "n":#See line 46
        
        model = input("\nWhich model of Samsung is it? (e.g Galaxy S7, Galaxy Note) ")#See line 48.
        global model#See line 190.
        confirmation = input("Samsung " + model + ",correct? (y/n) ")#See line 48.
        confirmation_lower = confirmation.lower()#See line 33.

        if confirmation_lower == "y":#See line 18
            main()#See line 33.
            break#See line 228.
        
        elif confirmation_lower == "n":#See line 20.
            samsung()#See line 33.
            break#See line 228.

def iphone():#See line 14.
    confirmation = 0#See line 160.
    

    while confirmation != "y" or confirmation != "n":#See line 46
        
        model = input("\nWhich model of iPhone is it? (e.g 5C, 6S+) " )#See line 48. 
        global model#See line 190.
        confirmation = input("iPhone " + model + ",correct? (y/n) ")#See line 48.
        confirmation_lower = confirmation.lower()#See line 33.

        if confirmation_lower == "y":#See line 18
            main()#See line 33.
            break#See line 228.
        
        elif confirmation_lower == "n":#See line 20.
            iphone()#See line 33.
            break#See line 228.

def phone_make():#See line 14.
    validation = 0#See line 160.
    print("\nOkay, what phone make is your device? (No numbers, just the brand.)")#See line 11.
    make = input("Phone make: ")#See line 48. 
    make_lower = make.lower()#See line 33.
    global make_lower#See line 190.
    
    if "iphone" in make_lower:#See line 18
        iphone()#See line 33.
        
    elif "samsung" in make_lower:#See line 20.
        samsung()#See line 33.

    elif "sony" in make_lower:#See line 20.
        sony()#See line 33.

    else: #The ELSE statement is only ran if none of the IF statements were satisfied.
        nothing_defined()#See line 33.
        
def user_details():#See line 14.
    print("\nFirst off, what is your name?")#See line 11.
    name = input("Name: ")#See line 48.
    global name#See line 190.
    print("\nOkay, now what is your email address?")#See line 11.
    email = input("Email: ")#See line 48.
    global email#See line 190.    

    confirmation = 0#See line 160.
    
    while confirmation != "y" or confirmation != "n":#See line 46

        confirmation = input("\nSo your name is " + name + " and your email is " + email + ", correct? (y/n) ") #By using + and a variable, it will print out whatever has been assigned to that variable. For example, if 'Shaun' was assigned to the variable 'name', then Shaun would be printed.
        confirmation_lower = confirmation.lower()#See line 33.

        if confirmation_lower == "y":#See line 18
            print("\nThank you for sharing your details. They will be kept on our secure server.")#See line 11.
            phone_make()#See line 33.
            break#See line 228.
            
        elif confirmation_lower == "n":#See line 20.
            user_details()#See line 33.
            break#See line 228.

user_details() #This is important to starting the code. Although all the def functions have been defined by this point, none have been referenced, and so calling one here starts off the chain of def functions.
