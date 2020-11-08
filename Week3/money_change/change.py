# Uses python3
import sys


def get_change(m):
    # write your code here
    # Returns the minimum number of coins given sizes 1, 5, 10
    d = int(m / 10)
    n = int((m - d*10) / 5)
    p = int(m - d*10 - n*5)
    m = d + n + p
    return m


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
