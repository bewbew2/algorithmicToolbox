# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    N = len(values)
    A = [0 for _ in range(N)]
    ratios = [values[i]/weights[i] for i in range(N)]
    ratios.sort(reverse=True)
    for i in range(N):
        if capacity == 0:
            return value, A
        a = min(weights[i], capacity)
        value += a*ratios[i]
        weights[i] = weights[i] - a
        A[i] += a
        capacity += -a

    return value


if __name__ == "__main__":
    # print("Hello. enter number and capacity")
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
