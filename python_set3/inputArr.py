#Getting input for array from user

from array import *
a = array("i",[])#empty array 
n = int(input("Enter the length of array "))
for i in range(n):
    x = int(input("Enter the next value "))
    a.append(x)
print (a)
