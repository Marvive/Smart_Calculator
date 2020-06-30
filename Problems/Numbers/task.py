# put your python code here
def multiply(*args):
    # if len(args) == 1:
    #     return args[0]
    # else:
    total = 1
    for i in args:
        total *= i
    return total


# print(multiply(int(input())))
