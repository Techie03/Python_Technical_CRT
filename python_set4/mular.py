#program for passing multiple arguments to a function
# Python program for passing
# multiple arguments to a function

# python program to find sum of any number
# of arguments passed to it
def findSum(*data):
    sumVal = 0
    for item in data:
       sumVal += item
    print("Sum of all arguments is ",sumVal)

# Calling function with variables...
findSum()
findSum(12)
findSum(12,4)
findSum(12,4,6)
findSum(1,2,3,4,5,6,7,8)
findSum(12,45,67,78,90,56)
