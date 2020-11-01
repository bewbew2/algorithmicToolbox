# Uses Python 3
"""
create an efficient fibonacci number generator and a naive comparison function
"""


# naive algorithm
def calc_fib(n):
    if n <= 1:
        return n
    return calc_fib(n - 1) + calc_fib(n - 2)


# only practical up to ~1E5 maybe. Get the fibonacci series
def fast_fib(n):
    # initial condition array 0..n
    fib = [i for i in range(0, n+1)]
    for i in range(2, n+1):
        fib[i] = fib[i - 1] + fib[i - 2]
    # print(fib)
    return fib[n]


# use mod 10 to get the last digit only
def last_fib(n):
    # initial condition array 0..n
    lib = [i for i in range(0, n+1)]
    for i in range(2, n+1):
        lib[i] = (lib[i - 1] + lib[i - 2]) % 10
    # print(lib)
    return lib[n]


if __name__ == '__main__':
    n = int(input())

    # print(calc_fib(n))
    # print(fast_fib(n))
    print(last_fib(n))
