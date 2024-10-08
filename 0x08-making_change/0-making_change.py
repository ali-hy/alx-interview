#!/usr/bin/python3
'''Make change dynamic programming problem'''


def makeChange(coins, total):
    '''Make change dynamic programming problem'''

    if total <= 0:
        return 0

    dp = [total + 1] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] <= total else -1
