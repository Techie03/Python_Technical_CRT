# Python program to illustrate valueError Exception 
import math

# Try Block Starts
try:
    # Taking input from the user ... 
    # The input needs to be a positive integer value...
    num1 = int(input("Enter number 1 : "))
    
    # finding the square root of the number. 
    # So the number cannot be negative.
    squareRoot = math.sqrt(num1)
    print("The Square root of the number is ",squareRoot)
    
# except block 
except ValueError as ex:
    print(ex)
