# python3
# implement the "fast algorithm" example but correct some issues

def max_pairwise_product_enh(numbers):
    n = len(numbers)
    index1 = 0
    for i in range(n):
        if numbers[i] > numbers[index1]:
            index1 = i
    if index1 == 0:
        index2 = 1
    else:
        index2 = 0

    for i in range(n):
        if (i != index1) & (numbers[i] > numbers[index2]):
            index2 = i

    return numbers[index1] * numbers[index2]


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product_enh(input_numbers))
