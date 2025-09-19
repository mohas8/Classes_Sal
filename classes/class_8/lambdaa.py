# def sum(a,b):
#     return a+b

sum = lambda a , b : a*b
#
#
#
print(sum(2,5))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2) # lambda a : a * 2

print(mydoubler(11))
