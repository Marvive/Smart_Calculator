import re


def has_numbers(input_string):
    return any(char.isdigit() for char in input_string)


def has_letters(input_string):
    return any(char.isalpha() for char in input_string)


nums = []
var_dict = {}
while "/exit" not in nums:
    nums = input()
    nums = nums.replace("^", "**")
    if "=" not in nums:
        num_list = nums.split()
    else:
        num_list = re.findall(r"[\w]+", nums)
        # num2_list = re.split(r"[\W]+", nums)
    # print("Found =")
    # print(num_list)
    # print(num2_list)

    if "/exit" in nums:
        print("Bye")
        break
    elif "/help" in nums:
        print("The program calculates the sum of numbers")
    elif not nums:
        continue

    if "=" in nums and not has_numbers(num_list[0]):

        if not has_numbers(num_list[-1]):
            try:
                var_dict[num_list[0]] = var_dict[num_list[-1]]
            except KeyError:
                print("Unknown Variable")
                continue
        else:
            if (has_numbers(num_list[-1]) and has_letters(num_list[-1]))\
                    or len(num_list) > 3:

                print("Invalid assignment")
                continue
            # elif len(num_list) > 3:
            #     print("Invalid assignment")
            #     continue
            else:
                var_dict[num_list[0]] = num_list[-1]

    elif "=" in nums and has_numbers(num_list[0]):
        print("Invalid identifier")
        continue

    elif len(num_list) == 1 and num_list[0] in var_dict:
        print(var_dict[num_list[0]])
    else:
        # Replaces variables with values from dictionary
        for i, j in enumerate(num_list):
            if j in var_dict:
                num_list[i] = var_dict[j]
            # elif j == "^":
            #     num_list[i] = "**"

        # print(num_list)
        try:
            print(eval("".join(num_list)))
        except SyntaxError:
            # print("Syntax Error")
            if nums.startswith("/"):
                print("Unknown command")
            else:
                print("Invalid expression")
        except NameError:
            print("Unknown Variable")
