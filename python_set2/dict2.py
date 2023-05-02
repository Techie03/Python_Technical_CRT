# Python program to create a dictionary with 
# key-value pairs using dict() function

# creating a dictionary
dict_a = dict(id = 101, name = 'Amit Kumar', Age = 21)

# printing the dictionary
print("dict_a :", dict_a)

# printing the length
print("Total elements: ", len(dict_a))

# printing the key-value pairs
for x, y in dict_a.items():
    print(x, ":", y)
