# Uses python3
import sys


def get_majority_naive(a):
    for i in range(n):
        ce = a[i]
        count = 0
        for j in range(n):
            if a[j] == ce:
                count += 1
        if count > n//2:
            return a[i]
    return -1


def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left - 1]
    # write your code here
    m = len(a)
    h = m//2
    left = get_majority_element(a[0:h], 0, h)
    right = get_majority_element(a[h:m], h, m)
    if a.count(left) > h:
        return left
    if a.count(right) > h:
        return right

    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
    # if get_majority_naive(a) != -1:
