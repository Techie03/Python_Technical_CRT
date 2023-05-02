def removeDuplicates (list1):
	# declare another list
	list2 = []

	# appending elements 
	for n in list1:
		if n not in list2:
			list2.append (n)
	return list2

# Main code
# declare a list
list1 = [10, 20, 10, 20, 30, 40, 30, 50]
# print the list 
print ("Original list: ", list1)
print ("List after duplicate remove: ", removeDuplicates (list1))
