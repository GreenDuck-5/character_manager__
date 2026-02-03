import sys
import time

def print_slow(text):
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.02)
    print()

def clear_screen():
    print("\033c", end="")

def continue_screen():
    input("Press Enter to continue...")

characters = []

def level_up(current_level, leveling):
    current_level += leveling
    if current_level > 15:
        current_level = 15
    return current_level

def skill_check(skill, current_skills):
    return skill not in current_skills

def determine_skill(leveling, current_level, skills):
    skills_earned = 0
    skills_list = [0, 0, 0]
    old_level = current_level - leveling
    for lvl in range(old_level + 1, current_level + 1):
        if lvl % 5 == 0:
            skills_earned += 1

    for _ in range(skills_earned):
        print("1. Sword Fighting\n2. Brawling\n3. Bow and Arrow")
        choice = input("Choose skill: ")
        if choice == "1" and skill_check("sword fighting", skills):
            skills_list[0] = 1
        elif choice == "2" and skill_check("brawling", skills):
            skills_list[1] = 1
        elif choice == "3" and skill_check("bow and arrow", skills):
            skills_list[2] = 1
    return skills_list

def point_reallocation(points, attributes):
    names = ["Strength", "Intelligence", "Wisdom", "Charisma"]
    while points > 0:
        for i in range(4):
            value = input(f"Add points to {names[i]}: ")
            if value.isdigit():
                value = int(value)
                if 0 <= value <= points:
                    attributes[i] += value
                    points -= value
    return attributes

def attribute_skill_menu(character):
    while True:
        print("1. Reallocate Attributes\n2. Level Up\n3. Exit")
        choice = input("Choose: ")

        if choice == "1":
            total = sum(character["attributes"])
            character["attributes"] = point_reallocation(total, [0, 0, 0, 0])

        elif choice == "2":
            leveling = int(input("How many levels gained: "))
            old_level = character["level"]
            character["level"] = level_up(old_level, leveling)
            character["attributes"] = point_reallocation(leveling, character["attributes"])
            skills_list = determine_skill(leveling, character["level"], character["skills"])

            if skills_list[0]:
                character["skills"].add("sword fighting")
                character["inventory"].add("sword")
            if skills_list[1]:
                character["skills"].add("brawling")
                character["inventory"].add("med pack")
            if skills_list[2]:
                character["skills"].add("bow and arrow")
                character["inventory"].add("bow")

        elif choice == "3":
            return

def character_search():
    if not characters:
        print("No characters found.")
        return

    print("Search by: name, race, class, level")
    key = input("Enter search type: ").lower()
    value = input("Enter value: ").title()

    matches = []
    for c in characters:
        if str(c[key]).title() == value:
            matches.append(c)

    if not matches:
        print("No matches.")
        return

    for i, c in enumerate(matches, 1):
        print(f"{i}. {c['name']}")

    choice = input("Select or press Enter: ")
    if not choice:
        return

    selected = matches[int(choice) - 1]
    if input("Delete character? yes/no: ").lower() == "yes":
        characters.remove(selected)
        print("Character deleted.")

def character_create():
    name = input("Name: ").title()
    race = input("Race (Human, Elf, Orc): ").title()
    char_class = input("Class (Fighter, Wizard, Rogue): ").title()

    attributes = [5, 5, 5, 5]
    if race == "Orc":
        attributes[0] += 3
    elif race == "Elf":
        attributes[1] += 3

    character = {
        "name": name,
        "race": race,
        "class": char_class,
        "level": 1,
        "attributes": attributes,
        "skills": set(),
        "inventory": {"starter weapon"}
    }

    characters.append(character)
    print("Character created.")

def character_inventory():
    if not characters:
        print("No characters available.")
        return

    for i, c in enumerate(characters, 1):
        print(f"{i}. {c['name']}")

    choice = input("Choose character: ")
    char = characters[int(choice) - 1]

    while True:
        print(char["inventory"])
        print("1. Add\n2. Remove\n3. Exit")
        option = input("Choose: ")

        if option == "1":
            char["inventory"].add(input("Item: ").lower())
        elif option == "2":
            char["inventory"].discard(input("Item: ").lower())
        elif option == "3":
            return

def character_manage():
    for i, c in enumerate(characters, 1):
        print(f"{i}. {c['name']}")
    choice = input("Choose character: ")
    attribute_skill_menu(characters[int(choice) - 1])

def main():
    while True:
        clear_screen()
        print("1. Search/Delete\n2. Create Character\n3. Inventory\n4. Attributes/Skills\n5. Exit")
        choice = input("Choose: ")

        if choice == "1":
            character_search()
        elif choice == "2":
            character_create()
        elif choice == "3":
            character_inventory()
        elif choice == "4":
            character_manage()
        elif choice == "5":
            exit()
        continue_screen()

print("Welcome to the RPG Character Manager")
continue_screen()
main()