# Python program to execute Python code 
# from a string

# string consisting of code 
codeStr = """print("Hello! Running python code from string")
a = 43
b = 3
print(a/b)"""	

# executing the code from string 
exec(codeStr)
