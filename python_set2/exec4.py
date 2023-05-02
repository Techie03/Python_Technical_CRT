# Program to illustrate IndexError Exception in Python...
try:
   employees = ["pankaj","amit","dilip","pooja","nitisha"]

   id = int(input("Enter Id (1-5):"))
   print("Your name is ",employees[id-1]," and your id is ",id)

# Value error if the values is not in range 
except ValueError as ex:
    print(ex)

# IndexError if the value is out of the list index...
except IndexError as ex:
    print(ex)
