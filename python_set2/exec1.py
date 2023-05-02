#Python exception handling program
#(Handling Type exception)

while True:
    try:
        num = int(input("Enter First Number: "))
        print(num)
        break
    except ValueError as e:
        print("Invalid Input..Please Input Integer Only..")
