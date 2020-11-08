# Uses python3
import sys


def gcd_naive(a_value, b_value):
    current_gcd = 1
    for d in range(2, min(a_value, b_value) + 1):
        if a_value % d == 0 and b_value % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd


def gcd_euclid(a_value, b_value):
    if b_value == 0:
        return a_value
    quotient, remainder = divmod(a_value, b_value)
    return gcd_euclid(b_value, remainder)


if __name__ == "__main__":
    gcd_input = sys.stdin.read()
    a, b = map(int, gcd_input.split())
    # print(gcd_naive(a, b))
    print(gcd_euclid(a, b))


