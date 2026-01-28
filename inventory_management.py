# MR 1st Pseudocode for Activity Diagram RPG
# Display INSTRUCTIONS for using the inventory and probably ask them if the want to go to their inventory menu

def inventory_menu():
    print("Welcome to your inventory menu!")
    print("You have the choice to go back to the main menu or stay")

    print( "1. Go back to main Menu")
    print( "2. Stay in Inventory Menu")
    stay_or_go = input(print("What would you like to do: "))

    if stay_or_go == '1':
        main()
    elif stay_or_go == '2':
        inventory_options()
    else:
        print("Please enter a valid Number.")
    pass
# Make a set for the items in the inventory
# Functions of the iunstructions and ask them if they want to go to  the menu or not
# IF yes call the inventory functions
# If the user chooses not take them back to the main function?
inventory_menu()
# A SET FOR THE ITEMS
inventory_items = {"starter weapon", "glass of water"}
inventory_possibilities = { "sword", "Med pack", " Bow and Arrow"}
# A FUNCTION for the Inventory Menu
# def inventory()

# Ask if they want to view, add , or remove from their inventory
# We will display the options of inventory that they already have
#ITEMS
def inventory_options():
    print("Hello, this is your inventory where you will find and store your items")
    print("Would you like to add, view, or remove from your inventory? ")

view_add_remove = input(print("What would you like to do ?")) 
#remove() 
def remove():
    print(inventory_items)
    pass
# take the list and number it
#Display the set
# ask what they want to remove
# After then display the new list

# add()
def add():
    print(inventory_items)
    pass
# Display the list
# Display add in options for the inventory
# Ask what they want to add - multiple choice
# Add it
# display the new list

def view():
    pass
    
# Ask them what they want to do
while True:
# IF user wants to view
#call the view function
    if view_add_remove == '1':
        view()
#Elif User wants to add
# call the add function
    elif view_add_remove == '2':
        add()

#Elif user wants to remove
# call the remove funtion
    elif view_add_more == '3':
        remove()
#Else,
#Enter something valid
    else:
        print("please enter a valid value.")
        break
