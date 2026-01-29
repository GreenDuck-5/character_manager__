#Skills and Attribute Management - Anna
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
        "2. Level up and you need to allocate new points\n" \
        "3. Level up and reallocate\n" \
        "4. Exit")
        #choice is ask if which they would like to do and they will input the matching number
        choice = input("Please input you choice number here: ")
        #if choice is 1 just reallocate
        if choice == "1":
            #points is the value of each of the attributes added up
            points = strength + intelligence + wisdom + charisma
            #change all attribute values in kwarg to 0
            #[strength, intelligence, wisdom, charisma]
            strength = 0
            intelligence = 0
            wisdom = 0
            charisma = 0
            #kwarg is call point_reallocation function with points and kwarg
            attributes_list = point_reallocation(points, strength, intelligence, wisdom, charisma)
            for num in range(4):
                kwarg["attributes"][num] = attributes_list[num]
        #elif choice is 2 or 3level up
        elif choice == "2" or choice == "3":
            #level in kwarg is level_up function
            print("The max level you can reach is 15 so don't add more than would sum to 15.")
            leveling = int(input("How much did you level up: "))
            if leveling < 0:
                print("You cannot level down.")
                return kwarg
            old_level = kwarg["level"]
            current_level = level_up(old_level, leveling)
            kwarg["level"] = current_level
            #skills_list = call determine skill function
            skills_list = determine_skill(leveling, current_level, skills=skills)
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
            #the skills in the kwarg are what was determined by the conditional
            #if choice is 3 level up and reallocate
            if choice == "3":
                #points is the value of each of the attributes plus the added points of leveling up
                strength, intelligence, wisdom, charisma = kwarg["attributes"]
                points = leveling
                #kwarg is call point_reallocation function with points and kwarg
                attributes_list = point_reallocation(points, strength, intelligence, wisdom, charisma)
            #points is the number of levels moved up
            for num in range(4):
                kwarg["attributes"][num] = attributes_list[num]
        #exit the function
        elif choice == "4":
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
def determine_skill(leveling, current_level,**kwarg):
    #intake leveling
    #skills is 0
    skills_earned = 0
    skill = kwarg["skills"]
    skills_list = [0,0,0]
    #if leveling is greater than 1
    if leveling > 1:
        #current_level += 1
        current_level += 1
        #for num in range(current level, current level + leveling )
        for num in range(current_level,current_level + leveling):
            #if num % 5 is 0 then add 1 to skill
            if num % 5 == 0:
                skills_earned += 1
            #if num % 5 isn't 0 then continue

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