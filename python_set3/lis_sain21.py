# declare list 
list1 = [10, 20, 10, 20, 30, 40, 30, 50]

# creating another list with unique elements
# declare another list 
list2 = []

# appending elements 
for n in list1:
	if n not in list2:
		list2.append(n)

# printing the lists 
print ("Original list")
print ("list1: ", list1)
print ("List after removing duplicate elements")
print ("list2: ", list2)
