#Python program to check if a tuple
#is a subset of another tuple
# Initializing and printing tuple 
tup1 = (4, 1, 6)
tup2 = (2, 4, 8, 1, 6, 5)
print("The elements of tuple 1 : " + str(tup1))
print("The elements of tuple 2 : " + str(tup2))

# Checking for subsets 
isSubset = (tup1).issubset(tup2)

if isSubset : 
    print("tup1 is a subset of tup2")
else : 
    print("tup1 is not a subset of tup2")
