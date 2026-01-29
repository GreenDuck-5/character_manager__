# MR 1st Pseudocode for Activity Diagram RPG
# Display INSTRUCTIONS for using the inventory and probably ask them if the want to go to their inventory menu

def main():
    print("\nYou are back at the main menu.\n")


def inventory_menu():
    print("Welcome to your inventory menu!")
    print("You have the choice to go back to the main menu or stay")

    print("1. Go back to main Menu")
    print("2. Stay in Inventory Menu")
    stay_or_go = input("What would you like to do: ")

    if stay_or_go == '1':
        main()
    elif stay_or_go == '2':
        inventory_options()
    else:
        print("Please enter a valid Number.")
        inventory_menu()
    pass


# Make a set for the items in the inventory
# Functions of the iunstructions and ask them if they want to go to  the menu or not
# IF yes call the inventory functions
# If the user chooses not take them back to the main function?

# A SET FOR THE ITEMS
inventory_items = {"starter weapon", "glass of water"}
inventory_possibilities = {"sword", "Med pack", "Bow and Arrow"}

# A FUNCTION for the Inventory Menu
# def inventory()

# Ask if they want to view, add , or remove from their inventory
# We will display the options of inventory that they already have
#ITEMS
def inventory_options():
    while True:
        print("Hello, this is your inventory where you will find and store your items")
        print("1. View Inventory")
        print("2. Add Item")
        print("3. Remove Item")
        print("4. Exit Inventory")

        view_add_remove = input("What would you like to do ? ")

        # Ask them what they want to do
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
        elif view_add_remove == '3':
            remove()

        #Else,
        #Enter something valid
        elif view_add_remove == '4':
            inventory_menu()
            break
        else:
            print("please enter a valid value to continue.")


#remove() 
def remove():
    print(inventory_items)

    # take the list and number it
    item_list = list(inventory_items)

    for i in range(len(item_list)):
        print(i + 1, item_list[i])

    #Display the set
    # ask what they want to remove
    choice = input("What number do you want to remove from your inevntory? ")

    if choice.isdigit():
        choice = int(choice)

        if 1 <= choice <= len(item_list):
            removed_item = item_list[choice - 1]
            inventory_items.remove(removed_item)
            print("Removed:", removed_item)
        else:
            print("Invalid number.")

    # After then display the new list
    print("Updated Inventory:", inventory_items)
    pass


# add()
def add():
    print(inventory_items)

    # Display the list
    possible_list = list(inventory_possibilities)

    # Display add in options for the inventory
    for i in range(len(possible_list)):
        print(i + 1, possible_list[i])

    # Ask what they want to add - multiple choice
    choice = input("What number do you want to add? ")

    if choice.isdigit():
        choice = int(choice)

        if 1 <= choice <= len(possible_list):
            selected_item = possible_list[choice - 1]
            inventory_items.add(selected_item)
            print("Added:", selected_item)
        else:
            print("Invalid number.")

    # Add it
    # display the new list
    print("Updated Inventory:", inventory_items)
    pass


def view():
    # Display the set
    print("Your Inventory:")
    for item in inventory_items:
        print(item)
    pass


inventory_menu()

