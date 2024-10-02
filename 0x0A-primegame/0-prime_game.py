#!/usr/bin/python3
"""Prime Game"""


def sieve(n: int) -> list:
    """ Returns a list of primes up to n using the Sieve of Eratosthenes. """
    is_prime = [True] * (n + 1)
    p = 2
    while (p * p <= n):
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    return [p for p in range(2, n + 1) if is_prime[p]]


def simulate_game(n: int) -> int:
    """ Simulates the game for a given n, returns 1 if Maria wins,
    0 if Ben wins. """
    primes = sieve(n)
    taken = [False] * (n + 1)
    turns = 0  # Count of turns taken

    for prime in primes:
        if not taken[prime]:  # If this prime is still available
            turns += 1  # Maria makes a move
            for multiple in range(prime, n + 1, prime):
                taken[multiple] = True  # Mark multiples as taken
    return 1 if turns % 2 == 1 else 0  # Odd turns mean Maria wins


def isWinner(x: int, nums: int) -> str:
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if simulate_game(n) == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
