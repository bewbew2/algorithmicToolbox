# Uses python3
import sys


def get_change(money):
    # write code to do the money change problem for denominations 1, 3, 4
    # minimum number of coins that changes money integer between 1 and 10E3
    # write your code here
    min_coins = [0 for _ in range(money + 1)]
    coins = [1, 3, 4]
    num_coins = 0
    for mon in range(1, money + 1):
        min_coins[mon] = 1E4
        for coin in coins:
            if mon >= coin:
                num_coins = min_coins[mon - coin] + 1
                if num_coins < min_coins[mon]:
                    min_coins[mon] = num_coins
    money = min_coins[mon]

    return money


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
