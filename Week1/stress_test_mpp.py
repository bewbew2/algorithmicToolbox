# import numpy as np
import random as rand
# import maximum_pairwise_product_3
# import maximum_pairwise_product_4
import maximum_pairwise_product_5
import maximum_pairwise_product_1


def stress_test(n_input, m_input):
    while 1:
        rand.seed(version=2)
        n = rand.randrange(2, n_input)
        a = []
        for i in range(0, n):
            a.append(rand.randrange(0, m_input))
        print(a)
        result1 = maximum_pairwise_product_1.max_pairwise_product_naive(a)
        result2 = maximum_pairwise_product_5.max_pairwise_product_sort(a)
        if result1 == result2:
            print("OK")
        else:
            print("Wrong answer ", result1, result2)
            return


if __name__ == "__main__":
    N = 5
    M = 6
    print(stress_test(N, M))
