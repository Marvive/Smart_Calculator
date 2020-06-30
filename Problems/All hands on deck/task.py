# nums = []
# for i in range(6):
#     ins = input()
#     if ins == "Jack":
#         ins = "11"
#     elif ins == "Queen":
#         ins = "12"
#     elif ins == "King":
#         ins = "13"
#     elif ins == "Ace":
#         ins = "14"
#     nums.append(ins)

dic = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
       "10": 10, "Jack": 11, "Queen": 12, "King": 13, "Ace": 14}

nums = []
for _i in range(6):
    ins = input()
    nums.append(dic[ins])

print(sum(nums) / 6)
