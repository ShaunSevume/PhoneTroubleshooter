#Centre number: 10854
#Candidate number: 7116
#Name: Shaun Sevume

import time #This will allow me to use the time.sleep function, which will make the program delay executing an insruction depending on how long I tell it to.
print("Welcome to the multicellular Troubeshooting program. If you have a problem with your phone, then you've come to the right place! Though we are only limited to a handful of \nsolutions, we hope to expand and solve everyone's problems in the future.")
time.sleep(2)#The program will wait two seconds before executing the next line as the time.sleep function delays the amount of time before the program executes the next line.
print("\nTo familiarize yourself with our program, we think it would be helpful if you enter your name.") #The \n makes a new line. It is used to make the text look neater.
time.sleep(1)#Delays the amount of time before the program executes the next line.
name = input("Name: ")#This will be where the user enters their name. This variable will be re-used in the code, and not only does it avoid repetition of asking for their name constantly, it makes the program more user-friendly, addressing by their name instead of just a user number.
time.sleep(1)#See lines 2 and 5. 
print("\nOkay " + name + ", we will give you a list of possible options. Remember, we are currently limited to only a few solutions, but hope to expand in the future. Please read the options \nbelow and enter the appropriate number.")

time.sleep(1)#See lines 7 and 9.

def feedback():#This is where a function is defined, to avoid repetition in the code. This way, you simply have to call this function when needed, instead of rewriting it.
    feedback = 0#The variable must be declared before being used in the while loop, so here it gets declared, but with no value since it isn't needed yet.
    while feedback != "y" or feedback != "n":#The while loop here means that until the answer is y or n, it will keep repeating.

        feedback = input("\nDid this solve your problem? (y/n)")#This is where the user gets to input an answer. Since it only accepts the inputs y and n, it will keep asking this question until the required input is recieved.
        feedback_lower = feedback.lower()#This converts the user's input into lowercase, so that it can match the case the if statements were written in.
        
        if feedback_lower == "y":#This statement will be run if the variable feedback_lower has a value of "y" (given by user input).
            print("We are glad to have helped you solve your issue," + name + "!")#Based on what the user entered for their name, we will be able to re-use their input and mention their name in this sentence.

        elif feedback == "n":#If the IF statement isn't valid, the program will move to the next statement, which in this case is an elif statement or, "else if".
            if option == "1":#The IF statement has a condition that must be met in order to run. In this case, the variable called 'option' has to have a value of a 1 (in string format however).
                print("\nCheck your phone for any damage. Severe damage may prevent it from working, (e.g dropping it from a high place or any kind of water damage) and if this is the case, you must go to the phone manufacturer's shop or a repair shop to get your phone looked at")

            elif option == "2":#See line 26.
                print("\nThere is most likley a problem with your charging port. You will have to take your phone to the manufacturer to get them to sort it out.") #Further help will be given to the user if their problem is still not solved. They may be also referred to a website.

            elif option == "3":#See line 26.
                print("\nThis could mean that your touch screen is broken, and you will have to get it replaced. If you do not wish to pay for a new touch screen, you can first try and factory reset the phone to see if that works.")

            elif option == "4":#See line 26.
                print("\nThis could mean a problem with your speakers. Go to your phone's manufacturer or repair shop for further assistance.")
               
            elif option == "5":#See line 26.
                 print("\nThis could mean a problem with your phone or network provider. could mean a problem with your phone or network provider. Contact your network provider about the issue after making sure your phone isn't the problem.")

            elif option == "6":#See line 26.
                 print("\nThis could mean a problem with your phone or network provider. Contact your network provider about the issue after making sure your phone isn't the problem.")

            elif option == "7":#See line 26.
                print("\nMobile data: Contact your netowork provider about your issue. \nWifi: Contact your ISP about your issue.")
            
            elif option == "8":#See line 26.
                print("\nThis could mean possible damage to your screen, possibly the light filters. This damage is repairable, but you will have to go to your phone's manufacturer store for further advice. If you really don't want to, you can always try a factory reset (since when your phone gets repaired they usually reset it anyway) before taking it to the phone's manufacturer.")

            elif option == "9":#See line 26.
                print("\nIf your phone has recently been dropped or has sustained water damage, this could cause problems with the microphone. However, it could simply be an app that prevents the mic from working properly. Either identify the app, or factory reset your phone, making sure to back up all of your data first. If these solutions don't work, this is an indication of your mic being broken, therefore you will have to go to your phone's maufacturer to try and repair it, or even replace it.")

        return_toMenu()#Here, the return_toMenu() function is called. This is on line 61.

def the_end():#See line 16.
    time.sleep(1)#See lines 7 and 9.
    print("\nHave a nice day!")#The print function is used to output text to the user.
    raise SystemExit #This terminates the program properly, so it isn't left running with nothing to display and nothing to be inputted.

def return_toMenu():#See line 16.
    time.sleep(1)#See lines 7 and 9.
    return1 = 0 #Before putting a variable in a while loop, this was necessary so that it was at least defined beforehand to prevent variable errors.

    while return1 != "y" or return1 != "n": #In this while loop, it will keep asking the user to return to the main menu until a valid input is entered.

        return1 = input("\nReturn to main menu?(y/n) ")#See line 20.
        return1_lower = return1.lower()#See line 21.
        
        if return1_lower == "y":#See line 27.
            main_menu()#Here, the main_menu() function is called.

        elif return1_lower == "n":#See line 26.
            the_end()#Here, the the_end() function is called.

def main_menu():#This is the main menu, where the user will be able to select their option. They will be taken back here if they choose to return to the main menu. These will first appear to the user and they will get to choose an option by entering a specific number.
    print("\n1.Your phone won't turn on \n2.Your phone won't charge \n3.Your phone's touch screen won't work \n4.Your phone does not play any sound. (This can include music or ringtones) \n5.Your phone is unable to place calls. \n6.Your phone is unable to send text messages \n7.Your phone is unable to connect to the internet \n8.Your phone's display is dim. \n9.Your phone's microphone isn't working properly \n10.Your problem is not listed above.")
    
    option = input("\nOption: ") #This will allow the user to input their option number, based on what they need to troubleshoot.
    global option #The variable option is a local variable. By using the global technique, it make the variable a global variable, meaning that it can be called in other functions.

    if option == "1":#See line 27.
        print("\nYour phone not turning on could be for a number of reasons. First, make sure it is charged. Leave it pluged in for at least 5-10 minutes before trying to turn it on. Another possibility is that you might not be holding down the power button for long enough. Try holding it down for at least 10 seconds to see if that helps.")
        time.sleep(5)#See lines 7 and 9.
        feedback()#This calls the feedback() function, which is above in the code.
        
    elif option == "2":#See line 26.
        print("\nTry using another cable and power adapter that you know works on another phone, to see if the problem lies with your phone or your charger. If your phone charges after this, then it was your charger that was the problem. If the phone isn't charging, this could mean there's something wrong with the charging port. check to see if there's any dust or things obstructing it, and make sure the charger fits in properly(not hanging loosley) and your battery works too.")
        time.sleep(5)#See lines 7 and 9.
        feedback()#See line 85.

    elif option == "3":#See line 26.
        print("\nIf you find your touch screen unresponsive, try starting with turning your device off and on again. If the touch screen only unresponsive in certain places, try to re-calibrate the screen (can be found in the settings of some phones) and see if it works.")
        time.sleep(5)#See lines 7 and 9.
        feedback()#See line 85.
       
    elif option == "4":#See line 26.
        print("\nMake sure you turn up your volume. This can be done by pressing the volume keys usually located on the side of your device. If not, try going to settings and looking for the option relating to sound.")
        time.sleep(5)#See lines 7 and 9.
        feedback()#See line 85.
        
    elif option == "5":#See line 26.
        print("\nSim Card: Make sure you have a SIM card inserted first! Unless you are attempting to call by internet, in which case, see option number 7. \nCredit: Make sure you have sufficient credit if you are on a pay as-you-go plan or you have sufficient minitues if you are on a monthly plan. \nCoverage: Make sure you have network coverage in your area. If not, try and move to an area with better coverage. If this still doesn't resolve your issue, talk to your network provider. \nValid Number: Make sure the number you want to call is valid and their phone is on. If not, a call will not take place.")
        time.sleep(5)#See lines 7 and 9.
        feedback()#See line 85.
        
    elif option == "6":#See line 26.
        print("\nSim Card: Make sure you have a SIM card inserted first! Unless you are attempting to text by internet, in which case, see option number 7. \nCredit: Make sure you have sufficient credit if you are on a pay as-you-go plan or you have sufficient texts if you are on a monthly plan. \nCoverage: Make sure you have network coverage in your area. If not, try and move to an area with better coverage. \nValid Number: Make sure the number you want to text is valid. If not, your text will not send.")
        time.sleep(5)#See lines 7 and 9.
        feedback()#See line 85.
        
    elif option == "7":#See line 26.
        print("\nMobile data: If you're using your mobile data (3G/4G usually), ensure you have netowork coverage (Usually displayed in a top corner of your phone) and that you have enough internet data on your sim Make sure mobile data is enabled in your phone's settings \nWifi: Make sure that you are within a suitable range of a wifi hotspot or hub and that wifi is enabled in your settings. Make sure the souce of wifi is turned on and connected to the internet. Ensure you have entered the wifi password beforehand and if you are tethered to another device, ensure you are within range and that it has enough internet data too.")
        time.sleep(5)#See lines 7 and 9.
        feedback()#See line 85.
      
    elif option == "8":#See line 26.
        print("\nThe first thing to do is check your screen brightness. There are different ways to do this, depending on your phone. For example, on an iPhone, you swipe upwards from the bottom and the slider should appear, whereas on andriod, you usually swipe downwards from the top once (or twice) and the slider should appear. However, on all devices, you can find this slider in the settings of your phone, most likley under the 'screen and display' option or something along those lines. Once the slider has been located, slide to the right nd the brightness should increase. Another thing to do is turn off auto brightness (if your phone has it) and manually control screen brightness.")
        time.sleep(5)#See lines 7 and 9.
        feedback()#See line 85. 
            
    elif option == "9":#See line 26.
        print("\nMake sure you know where your microphone is, as the location varies with devices. If you can't find it, look in the manual that should've come with your phone or go online to get a diagram your phone, that should indicate where the microphone is, along with other parts. Once you've located your microphone, check to see if there is anything obstructing it (e.g dust) and try to clean it out by either blowing gently into it or using a soft cloth (like a glasses' claeaner.)")
        time.sleep(5)#See lines 7 and 9.
        feedback()#See line 85.     
        
    elif option == "10":#See line 26.
        print("\nWe are very sorry to see that our program is unable to solve your problem," + name + ". In the future, we hope to improve it to solve an as wide range of problems as possible. For now, all we can suggest is searching the internet for your said problem, or simply go to your phone's manufacturer shop. A good place to begin your search is www.google.com. We hope you are able to solve your problem eventually!")
        return_toMenu()#See line 85.

    else:#The ELSE statement is only run if all the IF statements aren't satisfied.
        print("\nPlease enter a number between 1 and 10.")#See line 58.
        main_menu()#See line 71.

main_menu()#The whole code is indented so that when it reads the line main_menu() it goes back to the top. Since up until now the whole code has been defined as the main menu, we must tell python to actually print it now, after defining the code. It will still run normally, but will enable it to return to the top when we tell it to.

        
    

    
           

