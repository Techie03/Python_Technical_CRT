myTuple = (5, 1, 8, 3, 9)
print("The tuple elements are " + str(myTuple))
myList = [2, 4, 7, 8, 0]
print("The list elements are " + str(myList))

isPresent = False
for ele in myList:	
	if ele in myTuple :
		isPresent = True
		break
		
print("Is there any element in the list which is also present in tuple ? : " + str(isPresent))
