mark = { "john":85 , "hasan":100}

word = {"table" : "a piece of furniture"}

print(mark.keys())
print(mark.values())
print(mark.items())

mark.update({"hasan":81, "john":85})

print(word.get('table'))
# print(mark['hasan'])