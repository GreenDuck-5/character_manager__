#DJ, 1st, Character Search Function

#funciton to clear screen
def clear_screen(): print("\033c", end="")

#funciton to let user pick when to continue screen
def continue_screen(): input("Press \"Enter\" or \"Return\" to continue:\n")

# temp characters
characters = [
    {"name": "Aria", "class": "Wizard", "race": "Elf", "level": 5},
    {"name": "Brom", "class": "Fighter", "race": "Human", "level": 3},
    {"name": "Kara", "class": "Rogue", "race": "Halfling", "level": 4}
]

#Character Search Function:
def character_search(characters):

    # Give options on how to search: Class, Race, Name, Level
    search_options = ["class", "race", "name", "level"]

    while True:
        many_search = input("How many factors would you like to search by?: ")

        if many_search.isdigit():
            many_search = int(many_search)
            break
            
        else:
            print("Please enter valid input.")
            continue_screen()
            clear_screen()
            continue



    while True:
        print("How would you like to search?")
        #Search Function(User Input on "how to search"):
        print("Options: Class, Race, Name, Level")
        # Let user search:
        search_type = input("Enter search type: ").lower()

        if search_type not in search_options:
            print("Please enter valid input.")
            continue

        else: break

    search_value = input(f"Enter {search_type} to search for: ").title()
    
    matches = []

        # Loop through Characters:
    for character in characters:
            # If Character has the "how to search" requested by user:
        if str(character[search_type]).title() == search_value:
                # Print Character Name
                matches.append(character)

    if not matches:
        print("No chracters found.")
        return
    
    #print all charcaters
    print("Matching Characters:")
    for i, character in enumerate(matches, start = 1):
        print(f"{i}.) {character['name']}")
         

        # Let user select Character from list of Characters given:
        choice = input("Select a character number (or press Enter to cancel): ")
        if choice == "":
            return
        
        #cheack for valid input
        if not choice.isdigit() or int(choice) < 1 or int(choice) > len(matches):
             print("Invalid selection.")
             return
        
        selected_character = matches[int(choice) - 1]

            # Give User option on if they want to delete the Character:
        delete_choice = input(f"Do you want to delete {selected_character['name']}? (yes/no): ").lower()
        # If User picks "Yes":
        if delete_choice == "yes":
            #Delete character
            characters.remove(selected_character)
            print(f"{selected_character['name']} has been deleted.")
            return

character_search(characters)