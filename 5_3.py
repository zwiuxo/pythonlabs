n = int(input("Enter num"))
cities = {input() for city in range(n)}
new_city = input("Enter city")
if new_city in cities: print("REPEAT")
else: print("OK")