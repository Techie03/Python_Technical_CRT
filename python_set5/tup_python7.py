#Updating Each element in Tuple List

# Initializing and printing the list of tuples 

tupList = [(12, 8), (5, 2), (1, 3, 7, 8)]

print("The elements of list of tuple are " + str(tupList))
updateVal = 6

# Updating list of tuple by adding the given element
updatedList = [tuple(j + updateVal for j in tup ) for tup in tupList]

print("List after adding the update element to each element : " + str(updatedList))
