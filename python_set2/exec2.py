# Python program to illustrate ValueError Exception 
try:
    num1 = int(input("Enter number 1 : "))
    num2 = int(input("Enter number 2 : "))
    numSum = num1 + num2
    print("The sum of the two numbers is ",numSum)
    
# except block 
except ValueError as ex:
    print(ex)
