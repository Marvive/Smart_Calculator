from _collections import deque

actions = int(input())

my_stack = deque()
for _ in range(actions):
    action = input()
    if action.startswith("BUY"):
        my_stack.append(action[4:])
    else:
        print(my_stack.pop())
