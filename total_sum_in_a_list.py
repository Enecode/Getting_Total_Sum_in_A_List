numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def calculate_sum_of_list(number):
    total_sum = 0
    for i in range(0, len(numbers)):
        total_sum += numbers[i]

    return total_sum


result = calculate_sum_of_list(numbers)
print(result)