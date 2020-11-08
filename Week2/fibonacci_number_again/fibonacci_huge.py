# Uses python3
import sys


def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


def pisano(m_val):
    if m_val % 2 == 0:
        return m_val * 2
    else:
        return m_val * 4


def get_fibonacci_huge_efficient(n_val, m_val):
    if n_val <= 1:
        return n_val
    if m_val == 2:
        p_length = 3
    else:
        p_length = pisano(m_val)

    quotient, remainder = divmod(n_val, p_length)

    return get_fibonacci_huge_naive(remainder, p_length)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, m = map(int, input.split())
    # print(get_fibonacci_huge_naive(n, m))
    print(get_fibonacci_huge_efficient(n, m))
