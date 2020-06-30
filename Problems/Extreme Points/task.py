import json

# The following line creates a dictionary from the input. Do not modify it, please
test_dict = json.loads(input())

# Work with the 'test_dict'
# _list = list(test_dict.values())
# key_list = list(test_dict.keys())
#
# print(f"min: {key_list[_list.index(min(_list))]}")
# print(f"max: {key_list[_list.index(max(_list))]}")

print(f"min: {min(test_dict, key=test_dict.get)}")
print(f"max: {max(test_dict, key=test_dict.get)}")
