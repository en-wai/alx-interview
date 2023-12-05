# Prime Game Algorithm

## Overview

The Prime Game is a two-player game where Maria and Ben take turns eliminating numbers from a sequence based on prime factors. The player who successfully eliminates all numbers in a round wins that round. The player with the most round wins is the overall winner.

## Steps

1. **Define Helper Function `isPrime`**

    - Input: An integer `x`
    - Output: True if `x` is a prime number, False otherwise.

    ```python
    def isPrime(x):
        // Implementation details
    ```

2. **Define Helper Function `get_first_prime`**

    - Input: A list of integers `values`
    - Output: A new list containing numbers not divisible by the first prime number found in `values`.

    ```python
    def get_first_prime(values):
        // Implementation details
    ```

3. **Define Main Function `isWinner`**

    - Input:
        - An integer `x`: Number of rounds to be played.
        - A list of integers `nums`: Number of elements in each round.
    - Output: The name of the player who won the most rounds ('Maria' or 'Ben') or None if the number of rounds doesn't match the provided list.

    ```python
    def isWinner(x, nums):
        // Implementation details
    ```

4. **Initialize Scores for Maria and Ben**

    - Set `M` (Maria's score) and `B` (Ben's score) to 0.

    ```python
    M = {"Turn": True, "Score": 0}
    B = {"Turn": False, "Score": 0}
    ```

5. **Play Each Round**

    - Repeat the following steps for each round until `x` becomes 0:

        1. Set Ben's turn to `False` and Maria's turn to `True`.
        2. If the round index exceeds the length of the `nums` list, reset the round index to 0.
        3. Create a list `current` containing numbers from 1 to the current round's specified number (`nums[round]`).
        4. Eliminate numbers from `current` until only one remains, based on the `get_first_prime` function.
        5. Update scores based on the winner of the current round.

    ```python
    while x:
        // Implementation details
    ```

6. **Determine the Overall Winner**

    - Compare the final scores of Maria and Ben.
    - If Ben's score is less than Maria's score, return 'Maria' as the winner. Otherwise, return 'Ben'.

    ```python
    if B["Score"] < M["Score"]:
        return 'Maria'
    return 'Ben'
    ```

7. **End of Algorithm**

    - The algorithm concludes with the determination of the overall winner.

## Example Usage

```python
# Example Usage
rounds = 3
round_numbers = [4, 6, 8]
winner = isWinner(rounds, round_numbers)
print(f"The overall winner is: {winner}")
