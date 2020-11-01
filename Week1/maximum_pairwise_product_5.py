"""
get mpp by sorting
"""


def max_pairwise_product_sort(a):
    b = sorted(a)
    return b[-1] * b[-2]


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product_sort(input_numbers))
