# Python program to find uncommon words from two string,

# Getting strings as input from the user 
str1 = input('Enter first string : ')
str2 = input('Enter second string : ')

# finding uncommon words
str1Coll = str1.split()
str2Coll = str2.split()
uncommonWords = set(str1Coll).symmetric_difference(set(str2Coll))
  
# printing uncommon words 
print("All uncommon words from both the string are ", uncommonWords)
