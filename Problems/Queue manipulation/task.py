from _collections import deque

n = int(input())
deq = deque()

for _i in range(n):
    ops = input().split()
    if ops[0] == "ENQUEUE":
        deq.append(ops[1])
    else:
        deq.popleft()

print("\n".join(deq))
