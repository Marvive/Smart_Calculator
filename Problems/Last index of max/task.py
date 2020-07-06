def last_indexof_max(numbers):
    _max = max(numbers)
    for count, value in enumerate(numbers[::-1]):
        if value == _max:
            return len(numbers) - count - 1
    return None


def last_indexof_max_2(numbers):
    ind = []
    for x, y in enumerate(numbers):
        if y == max(numbers):
            ind.append(x)
    return max(ind)


def last_indexof_max_3(numbers):
    return max(x for x, y in enumerate(numbers) if y == max(numbers))


print(last_indexof_max_2([8, 11, 15, 15, 15, 12]))
print(last_indexof_max_3([8, 11, 15, 15, 15, 12]))
# nums = list(map(int, input().split()))
#
# # print(list(nums))
# print(last_indexof_max(nums))
