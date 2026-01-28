#Skills and Attribute Management - Anna
#I'm going to change all the kwarg spots to a list or a set
attributes_list = [0,0,0,0]
skills = {}
#attributes funtion
def attributes_func(**kwarg):
    #take all current attributes in the form of a kwarg
    inventory = kwarg["inventory"]
    attributes = kwarg["attributes"]
    strength = attributes[0]
    intelligence = attributes[1]
    wisdom = attributes[2]
    charisma = attributes[3]
    skills = kwarg["skills"]
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
    #elif choice is 2 or 3level up
    elif choice == "2" or choice == "3":
        #level in kwarg is level_up function
        print("The max level you can reach is 15 so don't add more than would sum to 15.")
        leveling = int(input("How much did you level up: "))
        current_level = kwarg["level"]
        current_level = level_up(current_level, leveling)
        #skills_list = call determine skill function
        skills_list = determine_skill(leveling, current_level)
        #if there are skills that were gained add items to inventory
        if skills_list != []:
            #use conditionals to interpet skills list
            if "sword fighting" in skills_list:
                skills.append("sword fighting")
                inventory.append("sword")
            if "brawling" in skills_list:
                skills.append("brawling")
                inventory.append("med pack")
            if "archery" in skills_list:
                skills.append("archery")
                inventory.append("bow and arrow")
        #the skills in the kwarg are what was determined by the conditional
        #if choice is 3 level up and reallocate
        if choice == "3":
            #points is the value of each of the attributes plus the added points of leveling up
            points = current_level + strength + intelligence + wisdom + charisma
            #kwarg is call point_reallocation function with points and kwarg
        attributes_list = point_reallocation(points, strength, intelligence, wisdom, charisma)
        #points is the number of levels moved up
    #return kwarg
        

#point_reallocation function
def point_reallocation(points, strength, intelligence, wisdom, charisma):
    #intake points as an agrument 
    attribute_list = [strength, intelligence, wisdom, charisma]
    #display all the attributes and there value
    print("You have the following attributes:\n" \
    "Strength\n" \
    "Intelligence\n" \
    "Wisdom\n" \
    "Charisma")
    print(f"You can reallocate you points anywhere. You have {points} to reallocate.")
        #tell then the value of points
        #while loop until points is 0
    while points > 0:
        
            #for each key in attributes
        for attribute in range(len(attribute_list)):
            attribute -= 1
                #iteration is true
            iteration = True
                #while loop until iteration is false
            while iteration == True:
                    #reallocate is asking the user how much they would like to add to this attribte
                reallocate = int(input(f"Please input the number of points you want to put in the {attribute_list[attribute]} attribute: "))
                    #make sure that the amout is within the points limit
                if reallocate <= points:
                    #if it is then the key is that number of reallocated
                    attribute_list[attribute] = reallocate                
                    #subtract the value of reallocated from points
                    points -= reallocate                        
                    #iteration is false
                    iteration = False
                    #if not then continue
                else:
                    continue
    #return kwarg
    return attribute_list

#level_up function
def level_up(current_level, leveling, skill):
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
    skills = 0
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
                skills += 1
            #if num % 5 isn't 0 then continue
    #specifics is an empty a list of three 0s
    specifics = [0,0,0]

    #while true
    while True:
        #for range(skills)
        for num in range(skills):
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
                add_value = skill_checker("brawling", skill)
                if add_value == True:
                    skill_list[1]
            elif choice == "3":
                add_value = skill_checker("bow and arrow", skill)
                if add_value == True:
                    skill_list[2]
            #add to the number in the coorisponding index in the list specifics
    #return specifics

#skill check function
    #intake skills and current skills
    #if that skill is in the current skills return false
    #else return true