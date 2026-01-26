# MR 1st Pseudocode for Activity Diagram RPG
# Display INSTRUCTIONS for using the inventory and probably ask them if the want to go to their inventory menu

def inventory_menu():
    print("Welcome to your inventory menu!")
    print("You have the choice to go back to the main menu or stay")

    print( "1. Go back to main Menu")
    print( "2. Stay in Inventory Menu")
    stay_or_go = input("What would you like to do: ")

    if stay_or_go == '1':
        main()
    elif stay_or_go == '2':
        invetory_options()
    else:
        print("Please enter a valid Number.")
    pass
# Make a set for the items in the inventory
# Functions of the iunstructions and ask them if they want to go to  the menu or not
# IF yes call the inventory functions
# If the user chooses not take them back to the main function?

# A SET FOR THE ITEMS

# A FUNCTION for the Inventory Menu
# def inventory()

# Ask if they want to view, add , or remove from their inventory
# We will display the options of inventory that they already have
#ITEMS

# Ask them what they want to do
# IF user wants to view
#call the view function

#Elif User wants to add
# call the add function

#Elif user wants to remove
# call the remove funtion

#Else,
#Enter something valid

# remove() 
# take the list and number it
#Display the set
# ask what they want to remove
# After then display the new list

# add()
# Display the list
# Display add in options for the inventory
# Ask what they want to add - multiple choice
# Add it
# display the new list