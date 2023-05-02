#program to call a function using keyword argument
def show(id="<no id>",name="<no name>"):
    print("Your id is :",id,"and your name is :",name)

show(12,"deepak")
show(name = "priya",id = 34)
