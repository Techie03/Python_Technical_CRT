print("Input a string: ")
str1 = input()

no_of_letters, no_of_digits = 0,0

for c in str1:
  no_of_letters += c.isalpha()
  no_of_digits += c.isnumeric()

print("Input string is: ", str1)
print("Total number of letters: ", no_of_letters)
print("Total number of digits: ", no_of_digits)
