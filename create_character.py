#AP 1st Period, Character Manager Pseudocode
import sys
import time
import random 

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(.05)

# Introduction function
def introduction():
    while True:
        print_slow("Welcome to Character Creation! \n here you will create a character that you will use throughout your journey.")
        print_slow("\nPlease choose what you would like to do below. ")

        print_slow(" \n1. Continue to create your character.")
        print_slow(" \n2. go back to main menu.")   
        
        choice = input(print_slow("\nwould you like to continue to create your character? or go back?(choose 1 or 2)")) 
    
        if choice == '1':
            character_creation()
        elif choice == '2':
            print("You are back at the main menu")
        else:
            print("Please enter a valid Value so you can continue.")
            break

#create function for creating character
def character_creation():
    while True:
        #Get the users choice for name, race, gender, and class
        name = input(print_slow("What is your character's name? "))
        #Make a list for attributes, all of which will automatically be set to 0 and in a predetermined spot so we can use the same index to know which number is which
        attributes = [0, 0] # Initialized with two 0s to prevent IndexError when accessing index 0 or 1
        races = {"Elf", "Human", "Orc"}
        inventory = [] # Defined inventory to prevent NameError
        print_slow(f" These are the available races: {races} ")
        char_race = ""
        while char_race not in races:
            char_race = input("Choose your race: ").capitalize()
            if char_race not in races:
                print("That race doesn't exist! Choose from the list.")
        
        char_class  = input(print_slow("What class would you like your character to be? "))
        # Adjust stats based on race
        if char_race == "Orc":
            attributes[0] += 5  # Bonus Strength
        elif char_race == "Elf":
            attributes[1] += 5  # Bonus Agility

        # Save as a single list (Character Profile)
        final_character = [name, char_race, char_class, attributes, inventory]
    
        print_slow("\nCharacter Summary Saved!")
        return final_character # Return data to be used elsewhere
            # Start the program

introduction()
