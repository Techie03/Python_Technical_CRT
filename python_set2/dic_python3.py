# Python program to create a dictionary # with integer keys
dict_a = {1 : "India", 2 : "USA", 3 : "UK", 4 : "Canada"}
print("Dictionary \'dict_a\' is...")
print(dict_a)

print("Dictionary \'dict_a\' keys...")
for x in dict_a:
    print(x)

print("Dictionary \'dict_a\' values...")
for x in dict_a.values():
    print(x)

print("Dictionary \'dict_a\' keys & values...")
for x, y in dict_a.items():
    print(x, ':', y)
