# the object_list has already been defined
# write your code here
# object_list = [1, "test", "test", "test", "blafasdlfka", [1, 2, 3]]
# object_list = [1, 397, 27468, -95, 1309, 397, -539874, -240767, -95, 397]

dict_start = {}

# counter = 0
for obj in object_list:
    try:
        hash(obj)
    except TypeError:
        continue
    else:
        if hash(obj) in dict_start:
            dict_start[hash(obj)] += 1
        else:
            dict_start[hash(obj)] = 1

count = 0
for values in dict_start.values():
    if values > 1:
        count += values

# print(dict_start)
print(count)
