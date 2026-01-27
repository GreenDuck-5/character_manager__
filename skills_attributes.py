#Skills and Attribute Management - Anna
#I'm going to change all the kwarg spots to a list or a set
attributes_list = [0,0,0,0]
skills = {}
#attributes funtion
def attributes(strength,intelligence,wisdom,charisma,level,*skills):
    #take all current attributes in the form of a kwarg
    inventory = {}
    #show them a menu of options about reallocation of attribute points
    print("This is the skills and attribute manager. You have the following options:\n" \
    "1. Reallocate existing points to differenct attributes\n" \
    "2. Level up and you need to allocate new points\n" \
    "3. Level up and reallocate")
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
        leveling = int(input("How much did you level up: "))
        current_level = level
        level = level_up(level, leveling)
        #skills_list = call determine skill function
        skills_list = determine_skill(leveling)
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
            #for each key in kwarg
        for attribute in attribute_list:
                #iteration is true
            iteration = True
                #while loop until iteration is false
            while iteration == True:
                    #reallocate is asking the user how much they would like to add to this attribte
                reallocate = input
                    #make sure that the amout is within the points limit
                    #if it is then the key is that number of reallocated
                    #subtract the value of reallocated from points
                    #iteration is false
                    #if not then continue
    #return kwarg

#level_up function
    #intake current level and how much they are leveling up
    #show that the max level is 15
    #add leveling to current level
    #if it is greater than 15 then subract what is extra
    #elif is less than 15 pass
    #return level
    
#determine_skills function
    #intake leveling
    #skills is 0
    #if leveling is greater than 1
        #current_level += 1
        #for num in range(current level, current level + leveling )
            #if num % 5 is 0 then add 1 to skill
            #if num % 5 isn't 0 then continue
    #specifics is an empty a list of three 0s
    #for range(skills)
        #let player choose based on the preset skills
        #add to the number in the coorisponding index in the list specifics
    #return specifics