# Python program to create a dictionary 
# with mixed keys

# creating the dictionary
dict_a = {1 : "India", 'city' : 'New Delhi', 
'Record' : {'id' : 101, 'name' : 'Amit', 'age': 21}}

# printing the dictionary
print("Dictionary \'dict_a\' is...")
print(dict_a)

# printing the keys only
print("Dictionary \'dict_a\' keys...")
for x in dict_a:
    print(x)

# printing the values only
print("Dictionary \'dict_a\' values...")
for x in dict_a.values():
    print(x)

# printing the keys & values
print("Dictionary \'dict_a\' keys & values...")
for x, y in dict_a.items():
    print(x, ':', y)

# printing the keys & values of Sub-Dictionary (Record)
print("Sub-Dictionary \'Record\' keys & values...")
for x, y in dict_a['Record'].items():
    print(x, ':', y)
