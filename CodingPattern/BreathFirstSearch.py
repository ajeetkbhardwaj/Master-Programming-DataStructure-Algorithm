"""
@author : ajeet kumar
@webpage : https://www.ajeetkbhardwaj.github.io
@Coding Pattern : Breadth First Search (BFS) technique to tranverse a tree

It was used to solve problems that involve traversing or searching through tree or graph data structures level by level order.
keep track of all nodes of a level using queue  before moving to the next level.
space complexity of algorithm will be O(N) where N is the max number of node in any level.

@problem-1 : 
Given a binary tree, populate an array to represent its level-by-level traversal. You should populate the values of all nodes of each level from left to right in separate sub-arrays.
@leetcode : https://leetcode.com/problems/binary-tree-level-order-traversal/
1. Condition : Tranverse all nodes of each level before moving onto the next level
#####################---Pseudo Code----###################
Given a tree with it's data structure as a class
Aim to perform an operation onto it that produces a special types of output

Operation LevelOrderForwardTraversal(root):
1.Input : root
2. Output : [[], [2, 4], []]
3. Result = []
4. If Root != NULL Then Return Result
5. Create Queue and add Root to the Queue
6. While Queue != NULL:
      level_size = length of queue
      current_level = []
      for _ in range(level_size) then 
7.        Node = Queue remove the front element from the queue(popleft)
8.        current_level.add(node)
9.        if node.left exits Then current_level.add(node.left)
10.       If node.right exits Then current_level.add(node.right)
11.   add Result(current_level)
12. return Result
@problem-2 : 
Given a binary tree, populate an array to represent its level-by-level traversal in reverse order, i.e., the lowest level comes first. You should populate the values of all nodes in each level from left to right in separate sub-arrays.
@leetcode : https://leetcode.com/problems/binary-tree-level-order-traversal-ii/




@problem-3 : Level averages in binary tree
https://leetcode.com/problems/average-of-levels-in-binary-tree/
Given a binary tree, populate an array to represent the averages of all of its levels



"""
#%%
# 1.0 Brute Force Approach
from collections import deque
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def level_order_traversal(root):
    result = []

    if not root:
        return result

    queue = deque([root])  # Initialize the queue with the root node
    
    while queue:
        level_size = len(queue)  # Number of nodes at the current level
        current_level = []

        for _ in range(level_size):
            node = queue.popleft()  # Get the front node from the queue
            current_level.append(node.value)  # Add its value to the current level

            # Add child nodes to the queue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(current_level)  # Append the current level to the result

    return result

# Example usage
root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)

print("Level order traversal:", level_order_traversal(root))

# 1.1 Optimized Approach
from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, value: Optional[int] = None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    # If root is None or root value is None, return empty list
    if root is None or root.value is None:
        return []

    queue = deque([root])
    levels = []

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            node = queue.popleft()

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

            current_level.append(node.value)

        levels.append(current_level)

    return levels

# --- Test Cases ---

# Test case 1
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(levelOrder(root))  # [[3], [9, 20], [15, 7]]

# Test case 2
root = TreeNode(1)
print(levelOrder(root))  # [[1]]

# Test case 3
root = TreeNode()  # root with value None
print(levelOrder(root))  # []



# 2.0 Brute Force Approach
from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, value: Optional[int] = None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def reverseLevelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    if root is None or root.value is None:
        return []

    queue = deque([root])
    levels = deque()  # Use deque to prepend each level efficiently

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            node = queue.popleft()

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

            current_level.append(node.value)

        levels.appendleft(current_level)  # Add current level at the beginning

    return list(levels)

# --- Test ---

root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.left.right = TreeNode(10)
root.right.right = TreeNode(5)

print(reverseLevelOrder(root))  # Output: [[9, 10, 5], [7, 1], [12]]


"""
Problem- ZigZag Traversal
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

Given a binary tree, populate an array to represent its zigzag level order traversal. 
You should populate the values of all nodes of the first level from left to right, 
then right to left for the next level 
and keep alternating in the same manner for the following levels.
"""