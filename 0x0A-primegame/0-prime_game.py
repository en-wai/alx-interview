#!/usr/bin/python3
"""
Prime Game Interview Question:
Script defines game
"""


def get_first_prime(values):
    """
    Return new list exempt those divisible by 1st prime num found.
    Args:
    - values (list): List of integers.

    Returns:
    - list: Filtered list of no not divisible by the 1st prime num found.

    Example:
    >>> get_first_prime([1, 2, 3, 4, 5, 6])
    [1, 2, 3, 5]
    """
    for i in values:
        if isPrime(i):
            return [v for v in values if v % i != 0]
    return False


def isPrime(x):
    """
    Check if a given number is a prime number.

    Args:
    - x (int): The number to check for primality.

    Returns:
    - bool: True if x is a prime number, False otherwise.

    Example:
    >>> isPrime(5)
    True
    >>> isPrime(4)
    False
    """
    if x < 2 or x == 4:
        return False
    for i in range(2, x // 2):
        if x % i == 0:
            return False
    return True


def isWinner(x, nums):
    """
    Determine winner of game based on rounds played and given list of numbers.

    Args:
    - x (int): No. of rounds to be played.
    - nums (list): Integers representing number of elements in each round.

    Returns:
    - str: Name player who won most rounds, or None.

    Example:
    >>> isWinner(3, [4, 6, 8])
    'Maria'
    """
    if x != len(nums):
        return None
    # Initialize scores for Maria (M) and Ben (B)
    M = {"Turn": True, "Score": 0}
    B = {"Turn": False, "Score": 0}
    round = 0
    # Iterate through each round
    while x:
        B["Turn"] = False
        M["Turn"] = True
        if round >= len(nums):
            round = 0
        current = [x for x in range(1, nums[round] + 1)]
        # Continue eliminating numbers until only one is left
        while len(current) > 1:
            if get_first_prime(current):
                current = get_first_prime(current)
                if M["Turn"]:
                    M["Turn"] = False
                    B["Turn"] = True
                else:
                    B["Turn"] = False
                    M["Turn"] = True
        # Update scores based on the winner of the current round
        if M["Turn"]:
            B["Score"] += 1
        else:
            M["Score"] += 1
        round += 1
        x -= 1
    # Determine the overall winner
    if B["Score"] < M["Score"]:
        return 'Maria'
    return 'Ben'
