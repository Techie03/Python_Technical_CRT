a = 5
b = 8
print((lambda: b, lambda: a)[a < b]())
