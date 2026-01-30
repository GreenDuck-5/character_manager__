#Main file containing user interface

def skills_attributes():
    #I'm going to change all the kwarg spots to a list or a set
    attributes_list = [0,0,0,0]

    kwarg = {"inventory":[],
    "skills": set(),
    "attributes":[0,0,0,0],
    "level": 0 }
    #attributes funtion
    def attributes_func(kwarg):
        attributes_list = kwarg["attributes"].copy()
        #take all current attributes in the form of a kwarg
        inventory = kwarg["inventory"]
        attributes = kwarg["attributes"]
        strength = attributes[0]
        intelligence = attributes[1]
        wisdom = attributes[2]
        charisma = attributes[3]
        skills = kwarg["skills"]
        while True:
            #show them a menu of options about reallocation of attribute points
            print("This is the skills and attribute manager. You have the following options:\n" \
            "1. Reallocate existing points to differenct attributes\n" \
            "2. Level up\n" \
            "3. Exit")
            #choice is ask if which they would like to do and they will input the matching number
            choice = input("Please input you choice number here: ")
            #if choice is 1 just reallocate
            if choice == "1":
                #points is the value of each of the attributes added up
                strength, intelligence, wisdom, charisma = kwarg["attributes"]
                points = strength + intelligence + wisdom + charisma
                    #kwarg is call point_reallocation function with points and kwarg
                attributes_list = point_reallocation(points, strength = 0, intelligence=0, wisdom=0, charisma=0)
                for num in range(4):
                    names = ["Strength", "Intelligence", "Wisdom", "Charisma"]
                    kwarg["attributes"][num] = attributes_list[num]
                    print(f"Your {names[num]} attribute has {attributes_list[num]} points")
            #elif choice is 2 or 3level up
            elif choice == "2":
                #level in kwarg is level_up function
                old_level = kwarg["level"]
                
                print("The max level you can reach is 15 so don't add more than would sum to 15.")
                print(f"Your current level is {old_level}")
                leveling = int(input("How much did you level up: "))

                if leveling < 0:
                    print("You cannot level down.")
                    return kwarg
                current_level = level_up(old_level, leveling)
                kwarg["level"] = current_level
                points = leveling
                attributes_list = point_reallocation(points, strength, intelligence, wisdom, charisma)
                #skills_list = call determine skill function
                skills_list = determine_skill(leveling, current_level, skills)
                #use conditionals to interpet skills list
                if skills_list[0] == 1:
                    skills.add("sword fighting")
                    inventory.append("sword")
                if skills_list[1] == 1:
                    skills.add("brawling")
                    inventory.append("med pack")
                if skills_list[2] == 1:
                    skills.add("archery")
                    inventory.append("bow and arrow")
                print("Your skills  are:")
                for skill in skills:
                    print(skill)
                #the skills in the kwarg are what was determined by the conditional
                #if choice is 3 level up and reallocate
                for num in range(4):
                    names = ["Strength", "Intelligence", "Wisdom", "Charisma"]
                    kwarg["attributes"][num] = attributes_list[num]
                    print(f"Your {names[num]} attribute has {attributes_list[num]} points")
            #exit the function
            elif choice == "3":
                return kwarg   
        
            

    #point_reallocation function
    def point_reallocation(points, strength, intelligence, wisdom, charisma):
        #intake points as an agrument 
        attribute_list = [strength, intelligence, wisdom, charisma]
        names = ["Strength", "Intelligence", "Wisdom", "Charisma"]
        #display all the attributes and there value
        print("You have the following attributes:\n" \
        "Strength\n" \
        "Intelligence\n" \
        "Wisdom\n" \
        "Charisma")
        print(f"You can reallocate you points anywhere. You have {points} to reallocate.")
            #tell then the value of points
        while points > 0:
        #for loop to loop through all the attributes
            for attribute in range(len(attribute_list)):
                        #reallocate is asking the user how much they would like to add to this attribte
                reallocate_input = input(f"Please input the number of points you want to put in the {names[attribute]} attribute: ")
                #make sure it is a correct answer
                if not reallocate_input.isdigit():
                    print("Please enter a whole number")
                    continue

                reallocate = int(reallocate_input)
                    #make sure that the amout is within the points limit
                if 0 <= reallocate <= points:
                    #if it is then the key is that number of reallocated
                    attribute_list[attribute] += reallocate                
                    #subtract the value of reallocated from points
                    points -= reallocate                        
                    #iteration is false
                    #if not then continue
                else:
                    print("You don't have enough points")
        #return kwarg
        return attribute_list

    #level_up function
    def level_up(current_level, leveling):
        #intake current level and how much they are leveling up
        #show that the max level is 15
        #add leveling to current level
        current_level += leveling
        #if it is greater than 15 then subract what is extra
        if current_level > 15:
            subtract = current_level - 15
            current_level -= subtract
        #return level
        return current_level
        
    #determine_skills function
    def determine_skill(leveling, current_level, skill):
        #intake leveling
        #skills is 0
        skills_earned = 0
        skills_list = [0,0,0]
        #if leveling is greater than 1
        old_level = current_level - leveling
        for num in range(old_level + 1, current_level + 1):
            if num % 5 == 0:
                skills_earned += 1

        #for range(skills)
        for num in range(skills_earned):
            #let player choose based on the preset skills
            print("""You can choose between the following skills:
            1. Sword Fighting
            2. Brawling
            3. Bow and Arrow""")
            choice = input("Enter the number of your choice here: ")
            if choice == "1":
                add_value = skill_check("sword fighting", skill)
                if add_value == True:
                    skills_list[0] = 1
            elif choice == "2":
                add_value = skill_check("brawling", skill)
                if add_value == True:
                    skills_list[1] = 1
            elif choice == "3":
                add_value = skill_check("bow and arrow", skill)
                if add_value == True:
                    skills_list[2] = 1
                elif add_value == False:
                    print("You already have that skill.")
            #add to the number in the coorisponding index in the list specifics
        #return specifics
        return skills_list

    #skill check function
    def skill_check(skill, current_skills):
        #intake skills and current skills
        answer = False
        #if that skill is in the current skills return false
        if skill not in current_skills:
            answer = True
        #else return true
        return answer
        
    attributes_func(kwarg)

def character_search():
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

def character_create():
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

def character_inventory():
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