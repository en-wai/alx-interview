#!/usr/bin/python3

def canUnlockAll(boxes):
    # Create a set to keep track of visited boxes.
    visited = set()
    
    # Initialize a stack for DFS and start with the first box (index 0).
    stack = [0]
    
    # Iterate through the stack while there are boxes to visit.
    while stack:
        box_index = stack.pop()
        
        # Mark the current box as visited.
        visited.add(box_index)
        
        # Iterate through the keys in the current box.
        for key in boxes[box_index]:
            # Check if the key opens a new box and if that box hasn't been visited yet.
            if key < len(boxes) and key not in visited:
                stack.append(key)
    
    # Check if all boxes have been visited.
    return len(visited) == len(boxes)

# Example usage:
if __name__ == "__main__":
    boxes = [[1], [2], [3], [0]]
    print(canUnlockAll(boxes))  # Output: True
