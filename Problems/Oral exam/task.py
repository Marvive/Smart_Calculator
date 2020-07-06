from _collections import deque

n = int(input())
deq = deque()

for _i in range(n):
    operation = input().split()
    if operation[0] == "READY":
        deq.append(operation[1])
    elif operation[0] == "PASSED":
        print(deq.popleft())
    else:
        deq.append(deq.popleft())
