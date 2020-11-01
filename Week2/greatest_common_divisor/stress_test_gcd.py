import random as rand
import gcd


def stress_test(n_input):
    while 1:
        rand.seed(version=2)
        a = rand.randrange(1, n_input)
        b = rand.randrange(1, n_input)
        result1 = gcd.gcd_naive(a, b)
        result2 = gcd.gcd_euclid(a, b)
        if result1 == result2:
            print("OK")
        else:
            print("Wrong answer ", result1, result2)
            return


if __name__ == "__main__":
    N = 50
    print(stress_test(N))
