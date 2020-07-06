import _collections as c

n = int(input())
stacked = c.deque()

for _i in range(n):
    operation = input().split()
    if len(operation) == 2:
        stacked.append(operation[1])
    else:
        stacked.pop()

for _i in reversed(stacked):
    print(_i)
# print("\n".join(stacked[::-1]))
# print(stacked)
