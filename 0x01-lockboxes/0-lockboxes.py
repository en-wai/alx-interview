#!/usr/bin/python3
"""
This function determines if all boxes can be opened.
It takes a list of lists, 'boxes', where each box may contain keys to other boxes.
A key with the same number as a box opens that box.
It returns True if all boxes can be opened, else it returns False.
"""

def canUnlockAll(boxes):
    """
    Checks if all boxes can be unlocked.
    
    Args:
        boxes (list of lists): A list of lists representing boxes and their keys.
        
    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    for key in range(1, len(boxes)):
        key_found = False
        for box_idx in range(len(boxes)):
            if key in boxes[box_idx] and key != box_idx:
                key_found = True
                break
        if not key_found:
            return False
    return True

# Example usage:
if __name__ == "__main__":
    boxes = [[1], [2], [3], [0]]
    print(canUnlockAll(boxes))  # Output: True

