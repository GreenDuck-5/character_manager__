#Skills and Attribute Management - Anna
#Pseudocode
#attributes funtion
    #take all current attributes in the form of a kwarg
    #show them a menu of options about reallocation of attribute points
    #choice is ask if which they would like to do and they will input the matching number
    #if choice is 1 just reallocate
        #points is the value of each of the attributes added up
        #change all attribute values in kwarg to 0
        #kwarg is call point_reallocation function with points and kwarg
    #elif choice is 2 or 3level up
        #level in kwarg is level_up function
        #skills_list = call determine skill function
        #if there are skills that were gained add items to inventory
        #use conditionals to interpet skills list
        #the skills in the kwarg are what was determined by the conditional
        #if choice is 3 level up and reallocate
            #points is the value of each of the attributes plus the added points of leveling up
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
    #intake current level
    #show that the max level is 15
    #leveling is ask how much they are leveling up
    #add to current level
    #if it is greater than 15 then subract what is extra
    #elif is less than 15 pass
    #return level
    
#determine_skills function
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


        





