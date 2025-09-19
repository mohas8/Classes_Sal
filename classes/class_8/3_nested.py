my_family = {
    "child1": {
        "name":"john",
        "age":10
    },
    "child2": {
            "name": "sal",
            "age":20
    }

}

# print(my_family["child2"]["age"])

for k, v in my_family.items():
    for y,z in v.items():
        print(y, z)

    # for k, v in v.items():
    #     print(k, v)
