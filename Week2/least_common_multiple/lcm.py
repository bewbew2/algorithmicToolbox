# Uses python3
import sys


def lcm_naive(a_value, b_value):
    for l in range(1, a_value * b_value + 1):
        if l % a_value == 0 and l % b_value == 0:
            return l

    return a_value * b_value


# re-use the Euclidean GCD for LCM
def gcd_euclid(a_value, b_value):
    if b_value == 0:
        return a_value
    quotient, remainder = divmod(a_value, b_value)
    return gcd_euclid(b_value, remainder)


# return the least common multiple of two numbers
def lcm_efficient(a_value, b_value):
    if a_value == b_value == 0:
        return 0
    return int(abs(a_value*b_value)/gcd_euclid(a_value, b_value))


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    # print(lcm_naive(a, b))
    print(lcm_efficient(a, b))


