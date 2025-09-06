fishes = ["rui", "elish", "pabda", "katla"]
is_pabda = False

for fish in fishes:
    if fish == "pabda":
        is_pabda = True
        break

if is_pabda:
    print("yes")
else:
    print("no")