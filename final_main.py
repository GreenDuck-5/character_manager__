import sys
import time
import random

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
characters.append({
    "info": ("Kael", "Human", "Wizard"),
    "level": 4,
    "attributes": [4, 10, 9, 6],
    "skills": {"bow and arrow"},
    "inventory": {"starter weapon", "spellbook", "mana potion"}
})

def level_up(current_level, leveling):
    current_level += leveling
    if current_level > 15:
        current_level = 15
    return current_level

def skill_check(skill, current_skills):
    return skill not in current_skills

def determine_skill(leveling, current_level, skills):
    skills_earned = 0
    old_level = current_level - leveling
    for lvl in range(old_level + 1, current_level + 1):
        if lvl % 5 == 0:
            skills_earned += 1

    new_skills = set()
    available_skills = ("sword fighting", "brawling", "bow and arrow")

    for _ in range(skills_earned):
        print_slow("1. Sword Fighting\n2. Brawling\n3. Bow and Arrow")
        choice = input("Choose skill: ")
        if choice in ("1", "2", "3"):
            skill_name = available_skills[int(choice) - 1]
            if skill_name not in skills:
                new_skills.add(skill_name)

    return new_skills

def point_reallocation(points, attributes):
    names = ["Strength", "Intelligence", "Wisdom", "Charisma"]

    def get_valid_points(name, remaining):
        while True:
            value = input(f"Add points to {name}: ")
            if value.isdigit():
                value = int(value)
                if 0 <= value <= remaining:
                    return value
            print_slow(f"Invalid input. Enter a number from 0 to {remaining}.")

    while points > 0:
        for i in range(4):
            if points <= 0:
                break
            value = get_valid_points(names[i], points)
            attributes[i] += value
            points -= value

    return attributes

def attribute_skill_menu(character):
    def display_menu():
        print_slow("1. Reallocate Attributes\n2. Level Up\n3. Exit")

    while True:
        display_menu()
        choice = input("Choose: ")

        if choice == "1":
            total = sum(character["attributes"])
            character["attributes"] = point_reallocation(total, [0, 0, 0, 0])
        elif choice == "2":
            leveling = int(input("How many levels gained: "))
            old_level = character["level"]
            character["level"] = level_up(old_level, leveling)
            character["attributes"] = point_reallocation(leveling, character["attributes"])
            new_skills = determine_skill(leveling, character["level"], character["skills"])
            for skill in new_skills:
                character["skills"].add(skill)
                if skill == "sword fighting":
                    character["inventory"].add("sword")
                elif skill == "brawling":
                    character["inventory"].add("med pack")
                elif skill == "bow and arrow":
                    character["inventory"].add("bow")
        elif choice == "3":
            return

def character_search():
    if not characters:
        print_slow("No characters found.")
        return

    print_slow("Search by: name, race, class, level")
    key = input("Enter search type: ").lower()
    value = input("Enter value: ").title()

    matches = []
    for c in characters:
        if key in ("name", "race", "class"):
            if str(c["info"][("name","race","class").index(key)]).title() == value:
                matches.append(c)
        elif key == "level":
            if str(c["level"]) == value:
                matches.append(c)

    if not matches:
        print_slow("No matches.")
        return

    for i, c in enumerate(matches, 1):
        print_slow(f"{i}. {c['info'][0]}")

    choice = input("Select or press Enter: ")
    if not choice:
        return

    selected = matches[int(choice) - 1]
    if input("Delete character? yes/no: ").lower() == "yes":
        characters.remove(selected)
        print_slow("Character deleted.")

def character_create():
    races = ("Human", "Elf", "Orc")
    classes = ("Fighter", "Wizard", "Rogue")

    name = input("Name: ").title()

    race = input(f"Race {races}: ").title()
    while race not in races:
        print_slow("Invalid race.")
        race = input(f"Race {races}: ").title()

    char_class = input(f"Class {classes}: ").title()
    while char_class not in classes:
        print_slow("Invalid class.")
        char_class = input(f"Class {classes}: ").title()

    base_attributes = (5, 5, 5, 5)
    attributes = list(base_attributes)

    if race == "Orc":
        attributes[0] += 3
    elif race == "Elf":
        attributes[1] += 3

    character = {
        "info": (name, race, char_class),
        "level": 1,
        "attributes": attributes,
        "skills": set(),
        "inventory": {"starter weapon"}
    }

    def generate_backstory(character):
        name, race, char_class = character["info"]
        strength, intelligence, wisdom, charisma = character["attributes"]
        skills = character["skills"]

        backstory = f"{name}, a {race} {char_class}, "

        if strength > intelligence and strength > wisdom:
            backstory += "has always relied on their formidable strength, "
        elif intelligence > strength and intelligence > wisdom:
            backstory += "is known for their sharp mind and clever strategies, "
        elif wisdom > strength and wisdom > intelligence:
            backstory += "has always been guided by wisdom and insight, "
        else:
            backstory += "is a well-rounded adventurer, "

        if "sword fighting" in skills:
            backstory += "wielding a sword with unmatched skill, "
        if "brawling" in skills:
            backstory += "adept at hand-to-hand combat, "
        if "bow and arrow" in skills:
            backstory += "deadly with bow and arrow, "

        if charisma > 7:
            backstory += "able to charm and inspire those around them, "
        if intelligence > 7:
            backstory += "with an intellect that outsmarts most foes, "
        if strength > 7:
            backstory += "possessing strength that few can rival, "

        backstory += "they venture into the world seeking adventure and glory."

        print_slow(backstory)

    characters.append(character)
    generate_backstory(character)
    print_slow("Character created.")

def character_inventory():
    if not characters:
        print_slow("No characters available.")
        return

    for i, c in enumerate(characters, 1):
        print_slow(f"{i}. {c['info'][0]}")

    choice = input("Choose character: ")
    char = characters[int(choice) - 1]

    while True:
        print_slow(char["inventory"])
        print_slow("1. Add\n2. Remove\n3. Exit")
        option = input("Choose: ")

        if option == "1":
            char["inventory"].add(input("Item: ").lower())
        elif option == "2":
            char["inventory"].discard(input("Item: ").lower())
        elif option == "3":
            return

def character_manage():
    for i, c in enumerate(characters, 1):
        print_slow(f"{i}. {c['info'][0]}")
    choice = input("Choose character: ")
    attribute_skill_menu(characters[int(choice) - 1])

def combat_simulator():
    if not characters:
        print_slow("No characters available to fight.")
        return

    for i, c in enumerate(characters, 1):
        print_slow(f"{i}. {c['info'][0]}")
    choice = input("Choose character for combat: ")
    char = characters[int(choice) - 1]

    enemy_health = 50 + char["level"] * 5
    char_health = 30 + char["attributes"][0] * 2  # Strength affects health

    print_slow(f"\n{char['info'][0]} enters combat with {enemy_health} enemy HP!\n")

    while enemy_health > 0 and char_health > 0:
        input("Press Enter to attack...")

        base_damage = char["attributes"][0]  # Strength
        if "sword fighting" in char["skills"]:
            base_damage += 5
        if "brawling" in char["skills"]:
            base_damage += 3
        if "bow and arrow" in char["skills"]:
            base_damage += 4

        damage = random.randint(base_damage // 2, base_damage)
        enemy_health -= damage
        print_slow(f"{char['info'][0]} deals {damage} damage! Enemy HP: {max(enemy_health,0)}")

        if enemy_health <= 0:
            print_slow("Enemy defeated! Victory!")
            break

        enemy_damage = random.randint(5, 10)
        char_health -= enemy_damage
        print_slow(f"Enemy hits back for {enemy_damage} damage! {char['info'][0]} HP: {max(char_health,0)}")

        if char_health <= 0:
            print_slow(f"{char['info'][0]} has been defeated...")
            break

def optimize_character(characters):
    name, race, char_class = character["info"]
    attributes = character["attributes"]
    skills = character["skills"]

    suggestions = []
    recommended_skills = []

    if char_class == "Fighter":
        suggestions.append("Prioritize Strength and Constitution")
        if "sword fighting" not in skills:
            recommended_skills.append("sword fighting")
        if "brawling" not in skills:
            recommended_skills.append("brawling")

    elif char_class == "Wizard":
        suggestions.append("Prioritize Intelligence and Wisdom")
        if "bow and arrow" not in skills:
            recommended_skills.append("bow and arrow")

    elif char_class == "Rogue":
        suggestions.append("Prioritize Dexterity (represented by Strength) and Charisma")
        if "bow and arrow" not in skills:
            recommended_skills.append("bow and arrow")
        if "brawling" not in skills:
            recommended_skills.append("brawling")

    if race == "Orc":
        suggestions.append("Use natural Strength bonus to focus on melee combat")
    elif race == "Elf":
        suggestions.append("Use Intelligence bonus to enhance ranged attacks or magic")

    print_slow(f"Optimization suggestions for {name}:")
    for s in suggestions:
        print_slow(f"- {s}")
    if recommended_skills:
        print_slow("Recommended skills to learn:")
        for skill in recommended_skills:
            print_slow(f"- {skill}")

def main(characters):
    while True:
        clear_screen()
        print_slow("1. Search/Delete\n2. Create Character\n3. Inventory\n4. Attributes/Skills\n5. Combat Simulator\n6. Suggest Optimizations\n7. Exit")
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
            combat_simulator()
        elif choice == "6":
            optimize_character(characters)
        elif choice == "7":
            exit()
        else:
            print_slow("Please enter valid input. 1-7")
            continue_screen()
            clear_screen()
            continue
        continue_screen()

print_slow("Welcome to the RPG Character Manager")
continue_screen()
main(characters)
