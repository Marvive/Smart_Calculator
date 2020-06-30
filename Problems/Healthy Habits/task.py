# walks = [
#     {"day": "Monday", "distance": 2000},
#     {"day": "Tuesday", "distance": 3000},
#     {"day": "Wednesday", "distance": 3500},
#     {"day": "Thursday", "distance": 2500},
#     {"day": "Friday", "distance": 2500},
#     {"day": "Saturday", "distance": 1000},
#     {"day": "Sunday", "distance": 5600}]

# the list "walks" is already defined
# your code here
denominator = len(walks)
total_distance = 0

for _, i in enumerate(walks, 1):
    total_distance += i["distance"]

print(total_distance // denominator)
