# list1 - first list with mixed type elements
# lists2 - second list with mixed type elements
list1 = ["Amit", "Shukla", 21, "New Delhi"]
list2 = ["Aman", "Shukla", 21, "Mumbai"]

# printing lists 
print ("list1:", list1)
print ("list2:", list2)

# finding and printing differences of the lists
print ("Elements not exists in list2:")
print (list (set(list1) - set (list2)))

print ("Elements not exists in list1:")
print (list (set(list2) - set (list1)))
