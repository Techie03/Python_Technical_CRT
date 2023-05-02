# Python program to add a tuple to list 

# Creating the List
myTuple = (9, 3, 1, 4)
# Printing the List 
print("Tuple Initially : " + str(myTuple))
# Creating Tuple
myList = [2, 6]

# Adding the tuple to list
addList = list(myTuple)
addList += myList
myTuple = tuple(addList)

# Printing resultant List
print("Tuple after Addition : " + str(myTuple))
