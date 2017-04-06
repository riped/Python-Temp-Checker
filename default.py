#===============================================================================
# Sean Corrigan 2017
# ICS 3U1
# Temp Checker
#===============================================================================

# import libraries
import os  # Needed for clearing the terminal in a clear manner
import time # Needed to sleep the system
#########
os.system("clear")
#########
def intro():
    print("Hey, I dont know who you are so imma call u 🅱️ ETER")
    UserName = input("Please enter your name 🅱️ ETER: \n")
    os.system("clear")
    if UserName == "sean":
        return 
    else:
        print("Hey,", UserName.title())
        time.sleep(3)
intro()
def askforcity():
    os.system("clear")
    numberofcities = input("How many cities would you like to compare?:\n")
    try:  # Try to convert to a int. if not restart
          numberofcities = int(numberofcities)  # Define as interger
    except ValueError:  # If it isn't a whole number then
        print("Sorry", numberofcities, "is not a valid number (ERRORCODE 1)")
        numberofcities = 1
        input("PRESS ENTER")
        askforcity()
    if numberofcities <= 1:
        input("You can't compare less then 2 citys silly (PRESS ENTER)")
        askforcity()
    numberoftries = 1

    
    my_array = []
    while numberoftries <= numberofcities:
        os.system("clear")
        print("Please enter city name", numberoftries)
        city = input("")
        print("Please enter the temprature for city", numberoftries)
        citytemp = input("")       
        try:  # Try to convert to a int. if not restart
          citytemp = int(citytemp)  # Define as interger
        except ValueError:  # If it isn't a whole number then
            input("PRESS ENTER TO RESTART")
            askforcity()
        
        my_array.append((citytemp, city))
        numberoftries = numberoftries ++ 1  # Add one to the end of the tries
        
    os.system("clear")
    min_temp, min_city = min(my_array)
    print(min_city.title(), "has lowest temperature:", min_temp)
    input("PRESS ENTER TO RESTART")
    askforcity()
        
    
askforcity()    

    
