#AP 1st Period, Character Manager Pseudocode
def introduction():
    while True:
        print("Welcome to Character Creation! ")
        print(" 1. Continue to create your character.")
        print(" 2. go back to main menu.")   
        choice = input("would you like to continue to create your character? or go back?") 
    
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
        pass
        #Make a list for attributes, all of which will automatically be set to 0 and in a predetermined spot so we can use the same index to know which number is which
        attributes = []
        #Get the users choice for name, race, gender, and class
        race = input("What race would you like your character to be? ")
        gender = input("What gender would you like your character to be? ")
        class_character = input("What class would you like your character to be? ")
        #Make another list for name, race, gender, and class, which will also have predetermined spots for which index they'll go in
        #Make a list for the inventory which will be blank to start
        #Adjust the stats and inventory based off of their race, class, etc.
        #Save all of it in a list so its saved together as one character
        final_character = []
        #return the list so you can access it outside of the function
        break