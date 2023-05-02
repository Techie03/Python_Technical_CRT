class AgeError(Exception):
    def __init__(self,message="Age must be greater than 0"):
        self.__errormessage=message
    def __str__(self):
        return(self.__errormessage)

try:
    age = int(input("Enter Age : "))
    if age<=0:
        # raise AgeError()
        raise AgeError("Age must be greater than zero")
    else:
        if age>=18:
            print("You are eligible to Vote")
        else:
            print("You are not eligible to Vote")

# except Block             
except AgeError as ex:
    print(ex)
