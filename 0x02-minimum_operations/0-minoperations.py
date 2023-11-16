#!/usr/bin/python3
"""Minimum Operations to Generate 'n' Characters of 'H'
"""


def min_operations_to_generate_n_characters(n: int) -> int:
    """Calculate the minimum operations needed to generate 'n' H characters.

    Args:
        n (int): The desired number of H characters.

    Returns:
        int: The minimum operations required.

    """
    current_sequence = 'H'
    base_sequence = 'H'
    operations_count = 0

    while len(current_sequence) < n:
        if n % len(current_sequence) == 0:
            operations_count += 2
            base_sequence = current_sequence
            current_sequence += current_sequence
        else:
            operations_count += 1
            current_sequence += base_sequence

    if len(current_sequence) != n:
        return 0

    return operations_count
