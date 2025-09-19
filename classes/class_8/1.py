dic = {
    "brand":"apple",
    "model":"m4",
    "year": 2025,
    "color":["red", "blue"]
}

# del dic["model"]
dic.clear()

# dic["birthday"]=2026

# dic.update({
#     "mode":"on",
#     "color":["green", "blue"]
# })

# print(dic.pop("year"))
x = dic.popitem()

# print(type(dic))
# print(dic["year"])
# print(len(dic))
# print(dic.get("model"))

# x = dic.keys()
# print(x)

print(dic)