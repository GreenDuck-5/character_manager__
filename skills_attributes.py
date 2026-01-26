#Skills and Attribute Management - Anna
#I'm going to change all the kwarg spots to a list or a set
#Pseudocode
#attributes funtion
def attributes(**kwarg):
    #take all current attributes in the form of a kwarg
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
        points = kwarg.get("strength") + kwarg.get("intelligence") + kwarg.get("wisdom") + kwarg.get("charisma")
        #change all attribute values in kwarg to 0
        kwarg["strength"] = 0
        kwarg["intelligence"] = 0
        kwarg["wisdom"] = 0
        kwarg["charisma"] = 0
        #kwarg is call point_reallocation function with points and kwarg
        kwarg = point_reallocation(points,**kwarg)
    #elif choice is 2 or 3level up
    elif choice == "2" or choice == "3":
        #level in kwarg is level_up function
        leveling = int(input("How much did you level up: "))
        current_level = kwarg["level"]
        kwarg["level"] = level_up(kwarg["level"], leveling)
        #skills_list = call determine skill function
        skills_list = determine_skill(leveling)
        #if there are skills that were gained add items to inventory
        if skills_list != []:
            #use conditionals to interpet skills list
            if "sword fighting" in skills_list:
                kwarg["skills"] += "sword fighting"
                kwarg["inventory"] += "sword"
            if "brawling" in skills_list:
                kwarg["skills"] += "brawling"
                kwarg["inventory"] += "med pack"
            if "archery" in skills_list:
                kwarg["skills"] += "archery"
                kwarg["inventory"] += "bow and arrow"
        #the skills in the kwarg are what was determined by the conditional
        #if choice is 3 level up and reallocate
        if choice == "3":
            #points is the value of each of the attributes plus the added points of leveling up
            points = current_level + kwarg.get("strength") + kwarg.get("intelligence") + kwarg.get("wisdom") + kwarg.get("charisma")
            #kwarg is call point_reallocation function with points and kwarg
        
        #points is the number of levels moved up
    #return kwarg
        

#point_reallocation function
    #intake points as an agrument and kwarg
    #display all the attributes and there value
        #tell then the value of points
        #while loop until points is 0
            #for each key in kwarg
                #iteration is true
                #while loop until iteration is false
                    #reallocate is asking the user how much they would like to add to this attribte
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