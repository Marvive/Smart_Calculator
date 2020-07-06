from _collections import deque

n = int(input())
deq = deque()
for _i in range(n):
    operation = input().split()
    if len(operation) > 1:
        deq.append(operation[1])
    else:
        deq.popleft()

print("\n".join(deq))
