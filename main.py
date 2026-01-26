#Main file containing user interface

def clear_screen(): print("\033c", end = "")

def continue_screen(): input("Press \"Enter\" or \"Return\" to continue:\n")

#Main function:
def main():
    while True:
        # Give options to do: Character Search, Character Create/Edit, Character Inventory, Exit
        option = input("What would you like to do?\n1.) Character Search\n2.) Character Create/Edit\n3.) Character Inventory\n4.) Exit")

        match option:

            # If the user picks Character Search:
            case "1":
                clear_screen()
                # Run Character Search Function
                character_search()
                # Restart Function
                continue

        # If the user picks Character Create/Edit:
            case "2":
                clear_screen()
                # Run Character Create Function
                character_create()
                # Restart Function
                continue

        # If the user picks Character Inventory:
            case "3":
                clear_screen()
                # Run Character Inventory Function
                character_inventory()
                # Restart Function
                continue

        # If the user picks Exit:
            case "4":
                clear_screen()
            # Exit Program
                exit()

        # If the user picks none of those:
            case _:
                clear_screen()
            # Print: "Please enter valid input"
                print("Please enter valid input.")
                continue_screen()
            # Restart Function
                continue

#Introduce the user
print("Hello User! This is MY character creator! Here you can make, remove, and edit characters! You can even search! Have fun!")

continue_screen()

# Run Main Function
main()