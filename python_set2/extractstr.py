# importing the module
import re

# string
string='''If you would like to get in touch with us through other ways, 
 please dail the number 6300340023. '''

# extracting the mobile number
Phonenumber=re.compile(r'\d\d\d\d\d\d\d\d\d\d\d\d')
m=Phonenumber.search(string)

# printing the result 
print('mobile number found from the string : ',m.group())
