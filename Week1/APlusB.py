# python3
# first assignment 

def sum_2_integers(digit1, digit2):
    return digit1 + digit2


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(sum_2_integers(a, b))
