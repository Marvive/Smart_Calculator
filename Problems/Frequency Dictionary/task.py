# put your python code here
what_it_do = input().lower().split()
dic = {}
for i in what_it_do:
    if i not in dic:
        dic[i] = 1
        # dic.update({i: 1})
    else:
        dic[i] += 1

for key, value in dic.items():
    print(f"{key} {value}")
