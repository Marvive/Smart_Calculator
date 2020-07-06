# put your python code here
from _collections import deque

deq = deque()
check = input()
out_message = ""
for i in check:
    try:
        if i == "(":
            deq.append(i)
        elif i == ")":
            deq.pop()
    except IndexError:
        out_message = "ERROR"
        break
if len(deq) > 0:
    out_message = "ERROR"

print("OK" if out_message != "ERROR" else out_message)
