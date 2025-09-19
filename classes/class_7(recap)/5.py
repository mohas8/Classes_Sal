x=5 #global variable
print(x)

def myFunction():
    def sayHello():
        print("hello")
    global y
    y = 5 #globa variable
    sayHello()
    print(x)
    # print(y)
#----
myFunction()
print(y)
