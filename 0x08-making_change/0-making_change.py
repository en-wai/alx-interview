#!/usr/bin/python3

"""
Interview Question on: fewest number of coins needed to
meet a given amount total
"""


def makeChange(coins, total):
    """
    Calculate the fewest number of coins needed to meet the total amount.

    Args:
    - coins (list): List of available coin denominations.
    - total (int): The target total amount.

    Returns:
    - int: The fewest number of coins needed to meet the total.
           Returns -1 if it's not possible to make exact change.
    """
    # If the total is non-positive, no coins are needed.
    if total <= 0:
        return 0

    # Sort the coins in descending order for optimization.
    coins.sort(reverse=True)

    change = 0  # Variable to track the total number of coins used.

    # Iterate through each coin denomination.
    for coin in coins:
        # Break the loop if the total has been met.
        if total <= 0:
            break

        # Calculate the maximum number of coins of the current denomination.
        temp = total // coin

        # Update the total number of coins used.
        change += temp

        # Update the remaining total after using the calculated coins.
        total -= (temp * coin)

    # If the total cannot be completely met with the available coins.
    if total != 0:
        return -1

    # Return the fewest number of coins needed to meet the total.
    return change
