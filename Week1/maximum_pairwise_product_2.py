# python3
# implement the "fast algorithm" example

def max_pairwise_product(numbers):
    n = len(numbers)
    index1 = 0
    for first in range(1, n):
        if numbers[first] > numbers[index1]:
            index1 = first
    index2 = 0
    for first in range(1, n):
        if (numbers[first] != numbers[index1]) and (numbers[first] > numbers[index2]):
            index2 = first

    return numbers[index1] * numbers[index2]


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
