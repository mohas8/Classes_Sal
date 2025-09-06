f = open("file.txt", "w")

f.write(" world")
f.close()

r = open("file.txt", "r")
data = r.read()

print(data)

