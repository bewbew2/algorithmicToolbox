# Uses python3
import sys
import random

#                            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16, 17, 18]
def partition3(a, l, n):
    i = l
    k = l
    p = n
    x = a[l]
    while i < p + 1:
        if a[i] < x:
            a[i], a[k] = a[k], a[i]
            k += 1
            i += 1
        elif a[i] == x:
            a[i], a[p] = a[p], a[i]
            p -= 1
        else:
            i += 1
    # a[l], a[k] = a[k], a[l]
    # before
    # l|<|<|<|<|<|k_|>|>|>|>|>|>|_p|=|=|=|n
    # after
    # l|<|<|<|<|<|m1|=|=|=|m2|>|>|>|>|>|>|n
    # a[q:n] == pivot
    # a[1:k-1] < a[q:n] < a[k:q-1]
    # m is the move count. Choose the smaller of the number equal or the number greater than
    m = min(p+1-k, n-(p+1)+1)
    m2 = k + n - i
    m1 = k
    # m1 = n - p
    # g = k + m - 1
    g = n - m + 1
    t = m1 + m
    while k < t:
        a[k], a[g] = a[g], a[k]
        g += 1
        k += 1
    return m1, m2


def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] < x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[i], a[j] = a[j], a[i]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m1, m2 = partition3(a, l, r)
    randomized_quick_sort(a, l, m1 - 1)
    randomized_quick_sort(a, m2 + 1, r)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
