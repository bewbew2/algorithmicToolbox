# python3
# implement the "faster algorithm"

def swap(ls, ind1, ind2):
    # swap list[ind1] with list[ind2]
    ls[ind1], ls[ind2] = ls[ind2], ls[ind1]
    return ls


def max_pairwise_product_fast(numbers):
    n = len(numbers) - 1
    index = 0
    for i in range(1, n):
        if numbers[i] > numbers[index]:
            index = i
    swap(numbers, index, n)
    index = 0
    for i in range(0, n):
        if numbers[i] > numbers[index]:
            index = i
    swap(numbers, index, n-1)
    return numbers[n-1] * numbers[n]


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product_fast(input_numbers))
