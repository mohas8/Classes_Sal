try:
    print(4/0)
except ZeroDivisionError:
    print("0 cant be at bottom")
else:
    print("other")
x=4
try:
    print(x)
except NameError:
    print("x is not defined ")
finally:
    print("finally will always be executed")