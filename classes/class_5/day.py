days=["saturday", "sunday", "monday", "tuestday", "wednesday", "friday"]

for day in days:
    if day == "friday":
        print(f"today is {day} ; no office")
        continue
    print(f"today is {day} ; go to office")