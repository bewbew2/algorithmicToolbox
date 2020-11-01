# import numpy as np
import random as rand
# import fibonacci_1
import fibonacci_2


# compare results of naive and fast fib with random input up to 45
def stress_test(n_input):
    while 1:
        rand.seed(version=2)
        n = rand.randrange(0, n_input)
        print(n)
        result1 = fibonacci_2.calc_fib(n)
        result2 = fibonacci_2.fast_fib(n)
        if result1 == result2:
            print("OK\r")
        else:
            print("Wrong answer ", result1, result2)
            return


if __name__ == "__main__":
    # less than or equal to 45
    N = 25
    print(stress_test(N))
