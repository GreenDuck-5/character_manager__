#Skills and Attribute Management - Anna
#Pseudocode
#attributes funtion
    #take all current attributes in the form of a kwarg
    #show them a menu of options about reallocation of attribute points
    #if not level up
        #points is the value of each of the attributes added up
        #call pointReallocation function
    #if level up and reallocate
        #points is the value of each of the attributes plus the added points of leveling up
        #call

#pointReallocation function
    #intake points as an agrument
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

