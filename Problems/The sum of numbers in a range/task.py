def range_sum(numbers, start, end):
    total = 0
    for number in numbers:
        if start <= number <= end:
            total += number
    return total


input_numbers = map(int, input().split())
a, b = map(int, input().split())
print(range_sum(input_numbers, a, b))
