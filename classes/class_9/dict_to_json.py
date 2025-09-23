import json

x = {
    "name":"Sal",
    "age":25
}

y=json.dumps(x, indent=4, separators=("?", "-->"), sort_keys=True)

print(y)