#program to return function from another function
# function - foo()
def foo():
    print("I am Foo")

# function - koo() returning foo
def koo():
    return foo

# calling the koo()
x=koo()
# calling function returned by koo()
x()
