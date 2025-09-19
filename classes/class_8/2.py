dic = {
    "brand":"apple",
    "model":"m4",
    "year": 2025,
    "color":["red", "blue"]
}
my_dict = dic.copy()

# print(dic.keys())
# print(dic.values())
#
for k,v in dic.items():
    print(k,v)

for k,v in my_dict.items():
    print(k,v)

# print(dic["brand"])
