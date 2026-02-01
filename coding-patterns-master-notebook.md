# Mastering 20 Essential Coding Patterns - Complete Notebook

## Table of Contents

1. [Two Pointers](#1-two-pointers)
2. [Island (Matrix Traversal) Pattern](#2-island-matrix-traversal-pattern)
3. [Fast &amp; Slow Pointers](#3-fast--slow-pointers)
4. [Sliding Window](#4-sliding-window)
5. [Merge Intervals](#5-merge-intervals)
6. [Cyclic Sort](#6-cyclic-sort)
7. [In-place Reversal of a Linked List](#7-in-place-reversal-of-a-linked-list)
8. [Tree Breadth First Search](#8-tree-breadth-first-search)
9. [Tree Depth First Search](#9-tree-depth-first-search)
10. [Two Heaps](#10-two-heaps)
11. [Subsets](#11-subsets)
12. [Modified Binary Search](#12-modified-binary-search)
13. [Bitwise XOR](#13-bitwise-xor)
14. [Top &#39;K&#39; Elements](#14-top-k-elements)
15. [K-way Merge](#15-k-way-merge)
16. [Topological Sort](#16-topological-sort)
17. [Trie](#17-trie)
18. [Backtracking](#18-backtracking)
19. [Monotonic Stack](#19-monotonic-stack)
20. [0/1 Knapsack (Dynamic Programming)](#20-01-knapsack-dynamic-programming)

---

## 1. Two Pointers

### Description

The Two Pointers technique uses two pointers traversing through data structures (arrays/linked lists) to solve problems efficiently. The pointers can move towards each other, in the same direction, or at different speeds.

### When to Use

- **Ordered Data Structures**: Arrays or lists that are sorted
- **Finding pairs/triplets**: With specific sum or properties
- **Palindrome checking**: Compare characters from both ends
- **Removing duplicates**: In sorted arrays

### Strategy

1. Initialize two pointers (usually at start and end, or both at start)
2. Move pointers based on problem conditions
3. Use the pointer positions to make decisions
4. Continue until pointers meet or cross

### Example Problem: Pair with Target Sum

**Problem**: Find a pair in a sorted array that adds up to a target sum.

**Pseudocode**:

```
function findPairWithTargetSum(arr, target):
    left = 0
    right = arr.length - 1
  
    while left < right:
        currentSum = arr[left] + arr[right]
      
        if currentSum == target:
            return [left, right]
        else if currentSum < target:
            left++  // Need larger sum
        else:
            right--  // Need smaller sum
  
    return [-1, -1]  // No pair found
```

### Time Complexity: O(n)

### Space Complexity: O(1)

### Practice Problems

1. **Squaring a Sorted Array**: Create sorted array of squares
2. **Triplet Sum to Zero**: Find all unique triplets that sum to zero
3. **Remove Duplicates**: Remove duplicates from sorted array in-place

### [Two Pointers Pattern Problem - LeetCode](https://leetcode.com/problem-list/two-pointers/)

---

## 2. Island (Matrix Traversal) Pattern

### Description

Used to navigate through 2D arrays/matrices to identify and process contiguous groups of elements (islands). Typically uses DFS or BFS to explore connected components.

### When to Use

- **Grid-based problems**: 2D matrix traversal
- **Connected components**: Finding grouped elements
- **Flood fill algorithms**: Changing connected regions
- **Counting islands**: Or similar grouped structures

### Strategy

1. Iterate through each cell in the matrix
2. When you find an unvisited target cell, start DFS/BFS
3. Mark all connected cells as visited
4. Count or process the connected component
5. Continue until all cells are processed

### Example Problem: Number of Islands

**Problem**: Count the number of islands in a 2D grid where '1' represents land and '0' represents water.

**Pseudocode**:

```
function numIslands(grid):
    if grid is empty:
        return 0
  
    rows = grid.length
    cols = grid[0].length
    islandCount = 0
  
    for i = 0 to rows-1:
        for j = 0 to cols-1:
            if grid[i][j] == '1':
                islandCount++
                dfs(grid, i, j)  // Mark entire island as visited
  
    return islandCount

function dfs(grid, row, col):
    if row < 0 or row >= grid.length or col < 0 or col >= grid[0].length:
        return
    if grid[row][col] == '0':
        return
  
    grid[row][col] = '0'  // Mark as visited
  
    // Explore all 4 directions
    dfs(grid, row-1, col)  // Up
    dfs(grid, row+1, col)  // Down
    dfs(grid, row, col-1)  // Left
    dfs(grid, row, col+1)  // Right
```

### Time Complexity: O(m × n)

### Space Complexity: O(m × n) for recursion stack

### Practice Problems

1. **Biggest Island**: Find the largest island by area
2. **Flood Fill**: Change color of connected region
3. **Surrounded Regions**: Capture surrounded regions

---

## 3. Fast & Slow Pointers

### Description

Uses two pointers moving at different speeds through a data structure. The fast pointer moves 2 steps while slow pointer moves 1 step, useful for cycle detection and finding middle elements.

### When to Use

- **Cycle detection**: In linked lists or arrays
- **Finding middle element**: Without knowing the length
- **Palindrome checking**: In linked lists
- **Start of cycle**: Detection problems

### Strategy

1. Initialize two pointers (slow and fast)
2. Move slow pointer by 1 step, fast pointer by 2 steps
3. If there's a cycle, pointers will eventually meet
4. Use meeting point to solve specific problems

### Example Problem: LinkedList Cycle

**Problem**: Determine if a linked list has a cycle.

**Pseudocode**:

```
function hasCycle(head):
    if head is null or head.next is null:
        return false
  
    slow = head
    fast = head
  
    while fast != null and fast.next != null:
        slow = slow.next
        fast = fast.next.next
      
        if slow == fast:
            return true  // Cycle detected
  
    return false  // No cycle
```

### Finding Cycle Start:

```
function findCycleStart(head):
    if not hasCycle(head):
        return null
  
    // Find meeting point
    slow = head
    fast = head
    while fast.next != null:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
  
    // Move one pointer to head, keep other at meeting point
    current = head
    while current != slow:
        current = current.next
        slow = slow.next
  
    return current  // Start of cycle
```

### Time Complexity: O(n)

### Space Complexity: O(1)

### Practice Problems

1. **Middle of LinkedList**: Find middle node
2. **Palindrome LinkedList**: Check if linked list is palindrome
3. **Happy Number**: Determine if number is happy

---

## 4. Sliding Window

### Description

Creates a window over a portion of data and slides it to solve problems efficiently. The window can be fixed-size or variable-size based on conditions.

### When to Use

- **Contiguous subarrays**: Finding max/min sum, length
- **Substring problems**: With specific properties
- **Fixed-size problems**: Maximum sum of k elements
- **Variable-size problems**: Smallest subarray with given sum

### Strategy

1. **Fixed Window**: Maintain window of fixed size k

   - Calculate result for first window
   - Slide window: remove leftmost, add rightmost
   - Update result
2. **Variable Window**: Expand/contract based on conditions

   - Expand window until condition is violated
   - Contract window until condition is satisfied
   - Track optimal result

### Example Problem: Maximum Sum Subarray of Size K

**Problem**: Find maximum sum of any contiguous subarray of size k.

**Pseudocode**:

```
function maxSumSubarray(arr, k):
    if arr.length < k:
        return -1
  
    // Calculate sum of first window
    windowSum = 0
    for i = 0 to k-1:
        windowSum += arr[i]
  
    maxSum = windowSum
  
    // Slide the window
    for i = k to arr.length-1:
        windowSum = windowSum - arr[i-k] + arr[i]
        maxSum = max(maxSum, windowSum)
  
    return maxSum
```

### Variable Window Example: Smallest Subarray with Given Sum

**Pseudocode**:

```
function smallestSubarrayWithSum(arr, targetSum):
    windowSum = 0
    minLength = infinity
    windowStart = 0
  
    for windowEnd = 0 to arr.length-1:
        windowSum += arr[windowEnd]
      
        // Contract window until sum is smaller than target
        while windowSum >= targetSum:
            minLength = min(minLength, windowEnd - windowStart + 1)
            windowSum -= arr[windowStart]
            windowStart++
  
    return minLength == infinity ? 0 : minLength
```

### Time Complexity: O(n)

### Space Complexity: O(1)

### Practice Problems

1. **Fruits Into Baskets**: Maximum fruits with 2 types
2. **Longest Substring with K Distinct**: Characters
3. **Longest Substring Without Repeating**: Characters

---

## 5. Merge Intervals

### Description

Deals with overlapping intervals by sorting and merging them based on specific conditions. Essential for time-based problems and scheduling.

### When to Use

- **Overlapping intervals**: Merging or finding overlaps
- **Scheduling problems**: Meeting rooms, appointments
- **Range problems**: Covering ranges efficiently
- **Interval insertion**: Adding new intervals

### Strategy

1. Sort intervals by start time
2. Initialize result with first interval
3. For each subsequent interval:
   - If it overlaps with last interval in result, merge them
   - Otherwise, add it to result
4. Return merged intervals

### Example Problem: Merge Intervals

**Problem**: Merge all overlapping intervals.

**Pseudocode**:

```
function mergeIntervals(intervals):
    if intervals.length <= 1:
        return intervals
  
    // Sort by start time
    sort(intervals, by start time)
  
    merged = []
    merged.add(intervals[0])
  
    for i = 1 to intervals.length-1:
        current = intervals[i]
        last = merged[merged.length-1]
      
        if current.start <= last.end:
            // Overlapping intervals, merge them
            last.end = max(last.end, current.end)
        else:
            // Non-overlapping interval
            merged.add(current)
  
    return merged
```

### Insert Interval Example:

```
function insertInterval(intervals, newInterval):
    result = []
    i = 0
  
    // Add all intervals before newInterval
    while i < intervals.length and intervals[i].end < newInterval.start:
        result.add(intervals[i])
        i++
  
    // Merge overlapping intervals
    while i < intervals.length and intervals[i].start <= newInterval.end:
        newInterval.start = min(newInterval.start, intervals[i].start)
        newInterval.end = max(newInterval.end, intervals[i].end)
        i++
  
    result.add(newInterval)
  
    // Add remaining intervals
    while i < intervals.length:
        result.add(intervals[i])
        i++
  
    return result
```

### Time Complexity: O(n log n) for sorting

### Space Complexity: O(n) for result

### Practice Problems

1. **Insert Interval**: Insert and merge new interval
2. **Intervals Intersection**: Find intersection of two interval lists
3. **Conflicting Appointments**: Check if person can attend all meetings

---

## 6. Cyclic Sort

### Description

Specialized in-place sorting algorithm for arrays containing numbers in a specific range (1 to n). Places each number at its correct index position.

### When to Use

- **Numbers in range 1 to n**: Or similar consecutive ranges
- **Finding missing numbers**: In sequence
- **Finding duplicates**: In range-based arrays
- **In-place sorting**: Without extra space

### Strategy

1. Iterate through array
2. For each number, check if it's at correct position
3. If not, swap it with number at its correct position
4. Continue until all numbers are in correct positions
5. Handle missing/duplicate numbers as needed

### Example Problem: Find Missing Number

**Problem**: Find missing number in array containing n distinct numbers from 0 to n.

**Pseudocode**:

```
function findMissingNumber(nums):
    n = nums.length
    i = 0
  
    // Place each number at its correct index
    while i < n:
        correctIndex = nums[i]
        if nums[i] < n and nums[i] != nums[correctIndex]:
            swap(nums, i, correctIndex)
        else:
            i++
  
    // Find the missing number
    for i = 0 to n-1:
        if nums[i] != i:
            return i
  
    return n  // Missing number is n
```

### Find All Duplicates Example:

```
function findDuplicates(nums):
    i = 0
  
    // Cyclic sort
    while i < nums.length:
        correctIndex = nums[i] - 1  // Numbers are 1 to n
        if nums[i] != nums[correctIndex]:
            swap(nums, i, correctIndex)
        else:
            i++
  
    // Find duplicates
    duplicates = []
    for i = 0 to nums.length-1:
        if nums[i] != i + 1:
            duplicates.add(nums[i])
  
    return duplicates
```

### Time Complexity: O(n)

### Space Complexity: O(1)

### Practice Problems

1. **Find All Missing Numbers**: In range 1 to n
2. **Find Duplicate Number**: Single duplicate in array
3. **Find Corrupt Pair**: Missing and duplicate numbers

---

## 7. In-place Reversal of a Linked List

### Description

Reverses linked list nodes without using additional memory by manipulating pointers. Can reverse entire list or sublists.

### When to Use

- **Reversing linked lists**: Complete or partial reversal
- **Palindrome checking**: Reverse half and compare
- **Reordering lists**: Specific patterns
- **Memory-efficient operations**: No extra space

### Strategy

1. Track previous, current, and next nodes
2. Reverse the link between current and previous
3. Move all three pointers forward
4. Continue until end of list/sublist

### Example Problem: Reverse a LinkedList

**Problem**: Reverse entire linked list.

**Pseudocode**:

```
function reverseLinkedList(head):
    previous = null
    current = head
  
    while current != null:
        next = current.next
        current.next = previous
        previous = current
        current = next
  
    return previous  // New head
```

### Reverse Sublist Example:

```
function reverseSubList(head, p, q):
    if p == q:
        return head
  
    // Skip first p-1 nodes
    current = head
    previous = null
    for i = 0 to p-2:
        previous = current
        current = current.next
  
    // Remember connections
    lastNodeOfFirstPart = previous
    lastNodeOfSubList = current
  
    // Reverse sublist
    next = null
    for i = 0 to q-p:
        next = current.next
        current.next = previous
        previous = current
        current = next
  
    // Connect with first part
    if lastNodeOfFirstPart != null:
        lastNodeOfFirstPart.next = previous
    else:
        head = previous
  
    // Connect with last part
    lastNodeOfSubList.next = current
  
    return head
```

### Time Complexity: O(n)

### Space Complexity: O(1)

### Practice Problems

1. **Reverse Every K-element Sub-list**: Reverse in groups of k
2. **Reverse Alternating K-element Sub-list**: Reverse alternate groups
3. **Rotate LinkedList**: Rotate by k positions

---

## 8. Tree Breadth First Search

### Description

Traverses tree level by level using a queue. Visits all nodes at current depth before moving to next depth level.

### When to Use

- **Level-order traversal**: Processing nodes by levels
- **Minimum depth**: Finding shortest path to leaf
- **Level-based operations**: Computing level averages, maximums
- **Tree serialization**: Level-order representation

### Strategy

1. Use queue to store nodes
2. Start with root in queue
3. While queue is not empty:
   - Process all nodes at current level
   - Add children of processed nodes to queue
4. Continue until queue is empty

### Example Problem: Binary Tree Level Order Traversal

**Problem**: Return level order traversal of binary tree.

**Pseudocode**:

```
function levelOrder(root):
    if root is null:
        return []
  
    result = []
    queue = []
    queue.add(root)
  
    while queue is not empty:
        levelSize = queue.size()
        currentLevel = []
      
        for i = 0 to levelSize-1:
            node = queue.remove()
            currentLevel.add(node.val)
          
            if node.left != null:
                queue.add(node.left)
            if node.right != null:
                queue.add(node.right)
      
        result.add(currentLevel)
  
    return result
```

### Zigzag Traversal Example:

```
function zigzagLevelOrder(root):
    if root is null:
        return []
  
    result = []
    queue = []
    queue.add(root)
    leftToRight = true
  
    while queue is not empty:
        levelSize = queue.size()
        currentLevel = []
      
        for i = 0 to levelSize-1:
            node = queue.remove()
          
            if leftToRight:
                currentLevel.add(node.val)
            else:
                currentLevel.addFirst(node.val)
          
            if node.left != null:
                queue.add(node.left)
            if node.right != null:
                queue.add(node.right)
      
        result.add(currentLevel)
        leftToRight = !leftToRight
  
    return result
```

### Time Complexity: O(n)

### Space Complexity: O(n)

### Practice Problems

1. **Reverse Level Order Traversal**: Bottom-up traversal
2. **Average of Levels**: Compute average at each level
3. **Minimum Depth**: Find minimum depth to leaf node

---

## 9. Tree Depth First Search

### Description

Traverses tree by going as deep as possible down branches before backtracking. Uses recursion or stack for implementation.

### When to Use

- **Path-based problems**: Finding paths with specific properties
- **Tree height/depth**: Computing maximum depth
- **Path sum problems**: Sum from root to leaf
- **Tree comparison**: Checking tree similarity

### Strategy

1. **Preorder**: Process node, then left subtree, then right subtree
2. **Inorder**: Process left subtree, then node, then right subtree
3. **Postorder**: Process left subtree, then right subtree, then node
4. Use recursion or explicit stack

### Example Problem: Binary Tree Path Sum

**Problem**: Check if tree has root-to-leaf path with given sum.

**Pseudocode**:

```
function hasPathSum(root, targetSum):
    if root is null:
        return false
  
    // Leaf node
    if root.left is null and root.right is null:
        return targetSum == root.val
  
    // Recursively check left and right subtrees
    return hasPathSum(root.left, targetSum - root.val) or
           hasPathSum(root.right, targetSum - root.val)
```

### All Paths for a Sum Example:

```
function findPaths(root, sum):
    allPaths = []
    findPathsRecursive(root, sum, [], allPaths)
    return allPaths

function findPathsRecursive(node, sum, currentPath, allPaths):
    if node is null:
        return
  
    currentPath.add(node.val)
  
    // Leaf node and path sum matches
    if node.left is null and node.right is null and sum == node.val:
        allPaths.add(currentPath.copy())
    else:
        // Continue searching in left and right subtrees
        findPathsRecursive(node.left, sum - node.val, currentPath, allPaths)
        findPathsRecursive(node.right, sum - node.val, currentPath, allPaths)
  
    currentPath.removeLast()  // Backtrack
```

### Time Complexity: O(n)

### Space Complexity: O(h) where h is height

### Practice Problems

1. **Sum of Path Numbers**: Sum all numbers formed by root-to-leaf paths
2. **Path with Given Sequence**: Check if sequence exists in tree
3. **Count Paths for Sum**: Count all paths with given sum

---

## 10. Two Heaps

### Description

Uses two priority queues (min-heap and max-heap) to maintain a balanced partition of numbers, typically for finding running median.

### When to Use

- **Running median**: As numbers are added dynamically
- **Balanced partitioning**: Maintaining two balanced groups
- **Sliding window median**: Median of subarrays
- **Optimization problems**: With heap-based solutions

### Strategy

1. **Max-heap**: Stores smaller half of numbers
2. **Min-heap**: Stores larger half of numbers
3. Keep heaps balanced (size difference ≤ 1)
4. Median is top of larger heap or average of both tops

### Example Problem: Find Median of Number Stream

**Problem**: Design class to calculate median of number stream.

**Pseudocode**:

```
class MedianFinder:
    function __init__():
        maxHeap = []  // Smaller half (max-heap)
        minHeap = []  // Larger half (min-heap)
  
    function addNumber(num):
        if maxHeap.isEmpty() or num <= maxHeap.top():
            maxHeap.add(num)
        else:
            minHeap.add(num)
      
        // Balance heaps
        if maxHeap.size() > minHeap.size() + 1:
            minHeap.add(maxHeap.removeTop())
        elif minHeap.size() > maxHeap.size() + 1:
            maxHeap.add(minHeap.removeTop())
  
    function findMedian():
        if maxHeap.size() == minHeap.size():
            return (maxHeap.top() + minHeap.top()) / 2.0
        else:
            return maxHeap.top() if maxHeap.size() > minHeap.size() else minHeap.top()
```

### Sliding Window Median Example:

```
function slidingWindowMedian(nums, k):
    result = []
  
    for i = 0 to nums.length - k:
        // Create window of size k
        window = nums[i:i+k]
        sort(window)
      
        // Find median
        if k % 2 == 1:
            median = window[k/2]
        else:
            median = (window[k/2-1] + window[k/2]) / 2.0
      
        result.add(median)
  
    return result
```

### Time Complexity: O(log n) for insertion

### Space Complexity: O(n)

### Practice Problems

1. **Sliding Window Median**: Median of all subarrays of size k
2. **Maximize Capital**: Choose projects to maximize profit
3. **Next Interval**: Find next interval for each interval

---

## 11. Subsets

### Description

Generates all possible combinations or subsets of a set using backtracking. Explores all ways to combine elements.

### When to Use

- **Combinatorial problems**: Generating all combinations
- **Power set**: All subsets of a set
- **Permutations**: All arrangements of elements
- **Decision problems**: Include/exclude each element

### Strategy

1. Use backtracking to explore all possibilities
2. For each element, make two choices: include or exclude
3. Recursively generate subsets for remaining elements
4. Base case: no more elements to process

### Example Problem: Generate All Subsets

**Problem**: Find all distinct subsets of a set.

**Pseudocode**:

```
function subsets(nums):
    result = []
    generateSubsets(0, nums, [], result)
    return result

function generateSubsets(index, nums, currentSubset, result):
    // Base case: processed all elements
    if index == nums.length:
        result.add(currentSubset.copy())
        return
  
    // Include current element
    currentSubset.add(nums[index])
    generateSubsets(index + 1, nums, currentSubset, result)
  
    // Exclude current element (backtrack)
    currentSubset.removeLast()
    generateSubsets(index + 1, nums, currentSubset, result)
```

### Iterative Approach:

```
function subsetsIterative(nums):
    subsets = [[]]  // Start with empty subset
  
    for num in nums:
        newSubsets = []
        for subset in subsets:
            newSubset = subset.copy()
            newSubset.add(num)
            newSubsets.add(newSubset)
        subsets.addAll(newSubsets)
  
    return subsets
```

### Permutations Example:

```
function permute(nums):
    result = []
    generatePermutations(nums, [], result)
    return result

function generatePermutations(nums, currentPermutation, result):
    if nums.isEmpty():
        result.add(currentPermutation.copy())
        return
  
    for i = 0 to nums.length-1:
        // Choose
        element = nums[i]
        currentPermutation.add(element)
        remainingNums = nums without element at index i
      
        // Explore
        generatePermutations(remainingNums, currentPermutation, result)
      
        // Unchoose (backtrack)
        currentPermutation.removeLast()
```

### Time Complexity: O(2^n) for subsets, O(n!) for permutations

### Space Complexity: O(2^n) for subsets, O(n!) for permutations

### Practice Problems

1. **Subsets with Duplicates**: Handle duplicate elements
2. **Combinations**: Generate all combinations of size k
3. **Letter Case Permutation**: Toggle case of letters

---

## 12. Modified Binary Search

### Description

Adapts binary search algorithm for various problems beyond simple searching in sorted arrays. Useful for finding boundaries and conditions.

### When to Use

- **Sorted arrays**: With modifications or rotations
- **Finding boundaries**: First/last occurrence of element
- **Range problems**: Finding elements in range
- **Peak finding**: In mountain arrays

### Strategy

1. Identify the search space and condition
2. Use binary search to eliminate half of search space
3. Adjust mid calculation and boundary conditions
4. Handle edge cases carefully

### Example Problem: Order-agnostic Binary Search

**Problem**: Binary search in array that could be ascending or descending.

**Pseudocode**:

```
function binarySearch(arr, target):
    start = 0
    end = arr.length - 1
  
    // Determine if array is ascending or descending
    isAscending = arr[start] < arr[end]
  
    while start <= end:
        mid = start + (end - start) / 2
      
        if arr[mid] == target:
            return mid
      
        if isAscending:
            if target < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:  // Descending order
            if target > arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
  
    return -1  // Not found
```

### Finding Ceiling of Number:

```
function findCeiling(arr, target):
    start = 0
    end = arr.length - 1
  
    if target > arr[end]:
        return -1  // No ceiling exists
  
    while start <= end:
        mid = start + (end - start) / 2
      
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
  
    return start  // Ceiling index
```

### Search in Rotated Array:

```
function searchRotated(arr, target):
    start = 0
    end = arr.length - 1
  
    while start <= end:
        mid = start + (end - start) / 2
      
        if arr[mid] == target:
            return mid
      
        // Left half is sorted
        if arr[start] <= arr[mid]:
            if target >= arr[start] and target < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:  // Right half is sorted
            if target > arr[mid] and target <= arr[end]:
                start = mid + 1
            else:
                end = mid - 1
  
    return -1
```

### Time Complexity: O(log n)

### Space Complexity: O(1)

### Practice Problems

1. **Find Range**: First and last position of element
2. **Search in Infinite Array**: Binary search in infinite sorted array
3. **Minimum in Rotated Array**: Find minimum element

---

## 13. Bitwise XOR

### Description

Uses XOR bitwise operator to solve problems efficiently. XOR has unique properties: a ⊕ a = 0, a ⊕ 0 = a, and is commutative/associative.

### When to Use

- **Finding unique elements**: In arrays with duplicates
- **Missing number problems**: Using XOR properties
- **Bit manipulation**: Flipping bits efficiently
- **Duplicate detection**: Finding odd occurrences

### Strategy

1. Leverage XOR properties: x ⊕ x = 0, x ⊕ 0 = x
2. XOR all elements to cancel out duplicates
3. Use bit manipulation for efficient solutions
4. Combine with other techniques for complex problems

### Example Problem: Single Number

**Problem**: Find the number that appears only once while others appear twice.

**Pseudocode**:

```
function singleNumber(nums):
    result = 0
  
    for num in nums:
        result = result XOR num
  
    return result  // All duplicates cancel out
```

### Two Single Numbers Example:

```
function findTwoSingleNumbers(nums):
    // XOR all numbers
    xorAll = 0
    for num in nums:
        xorAll = xorAll XOR num
  
    // Find rightmost set bit
    rightmostSetBit = 1
    while (xorAll AND rightmostSetBit) == 0:
        rightmostSetBit = rightmostSetBit << 1
  
    // Divide numbers into two groups and XOR separately
    num1 = 0
    num2 = 0
    for num in nums:
        if (num AND rightmostSetBit) != 0:
            num1 = num1 XOR num
        else:
            num2 = num2 XOR num
  
    return [num1, num2]
```

### Missing Number Example:

```
function findMissingNumber(nums):
    n = nums.length
  
    // XOR all numbers from 1 to n+1
    xorAll = 1
    for i = 2 to n+1:
        xorAll = xorAll XOR i
  
    // XOR with all numbers in array
    for num in nums:
        xorAll = xorAll XOR num
  
    return xorAll  // Missing number
```

### Time Complexity: O(n)

### Space Complexity: O(1)

### Practice Problems

1. **Complement of Base 10 Number**: Find binary complement
2. **Flipping an Image**: Flip and invert binary matrix
3. **Find Difference**: Between two strings

---

## 14. Top 'K' Elements

### Description

Finds the K largest or smallest elements using heaps (priority queues). Efficient for maintaining top K elements without sorting entire dataset.

### When to Use

- **Finding extremes**: K largest/smallest elements
- **Streaming data**: Maintaining top K in real-time
- **Frequency problems**: K most frequent elements
- **Distance problems**: K closest points

### Strategy

1. **K Largest**: Use min-heap of size K
2. **K Smallest**: Use max-heap of size K
3. Maintain heap size ≤ K by removing inappropriate elements
4. Final heap contains top K elements

### Example Problem: Top K Numbers

**Problem**: Find K largest numbers in array.

**Pseudocode**:

```
function findKLargest(nums, k):
    minHeap = []
  
    for num in nums:
        minHeap.add(num)
      
        if minHeap.size() > k:
            minHeap.removeMin()
  
    result = []
    while not minHeap.isEmpty():
        result.add(minHeap.removeMin())
  
    return result
```

### Kth Smallest Number Example:

```
function findKthSmallest(nums, k):
    maxHeap = []
  
    for num in nums:
        maxHeap.add(num)
      
        if maxHeap.size() > k:
            maxHeap.removeMax()
  
    return maxHeap.top()  // Kth smallest element
```

### K Closest Points to Origin:

```
function kClosestPoints(points, k):
    maxHeap = []  // Store (distance, point)
  
    for point in points:
        distance = sqrt(point.x^2 + point.y^2)
      
        if maxHeap.size() < k:
            maxHeap.add((distance, point))
        elif distance < maxHeap.top().distance:
            maxHeap.removeMax()
            maxHeap.add((distance, point))
  
    result = []
    while not maxHeap.isEmpty():
        result.add(maxHeap.removeMax().point)
  
    return result
```

### Time Complexity: O(n log k)

### Space Complexity: O(k)

### Practice Problems

1. **K Most Frequent Elements**: Find k most frequent numbers
2. **Sort Characters by Frequency**: Rearrange string by frequency
3. **Rearrange String**: No two same characters adjacent

---

## 15. K-way Merge

### Description

Merges K sorted arrays/lists into single sorted list using a min-heap to efficiently find the smallest element among K arrays.

### When to Use

- **Multiple sorted arrays**: Merging into one sorted array
- **External sorting**: Large datasets split into sorted chunks
- **Finding ranges**: Smallest range covering elements from K lists
- **Kth smallest**: In multiple sorted arrays

### Strategy

1. Use min-heap to track smallest unprocessed element from each array
2. Extract minimum from heap and add to result
3. Add next element from same array to heap
4. Continue until all arrays are processed

### Example Problem: Merge K Sorted Lists

**Problem**: Merge K sorted linked lists.

**Pseudocode**:

```
function mergeKLists(lists):
    if lists is empty:
        return null
  
    minHeap = []
  
    // Add first node from each list to heap
    for list in lists:
        if list != null:
            minHeap.add((list.val, list))
  
    dummy = ListNode(0)
    current = dummy
  
    while not minHeap.isEmpty():
        value, node = minHeap.removeMin()
        current.next = node
        current = current.next
      
        if node.next != null:
            minHeap.add((node.next.val, node.next))
  
    return dummy.next
```

### Kth Smallest in M Sorted Lists:

```
function findKthSmallest(lists, k):
    minHeap = []
  
    // Add first element from each list
    for i = 0 to lists.length-1:
        if lists[i].length > 0:
            minHeap.add((lists[i][0], 0, i))  // (value, index, listIndex)
  
    count = 0
    while not minHeap.isEmpty():
        value, index, listIndex = minHeap.removeMin()
        count++
      
        if count == k:
            return value
      
        // Add next element from same list
        if index + 1 < lists[listIndex].length:
            nextValue = lists[listIndex][index + 1]
            minHeap.add((nextValue, index + 1, listIndex))
  
    return -1
```

### Smallest Range Covering K Lists:

```
function smallestRange(lists):
    minHeap = []
    maxValue = -infinity
  
    // Initialize heap with first element from each list
    for i = 0 to lists.length-1:
        minHeap.add((lists[i][0], 0, i))
        maxValue = max(maxValue, lists[i][0])
  
    rangeStart = 0
    rangeEnd = infinity
  
    while minHeap.size() == lists.length:
        minValue, index, listIndex = minHeap.removeMin()
      
        // Update range if current is smaller
        if maxValue - minValue < rangeEnd - rangeStart:
            rangeStart = minValue
            rangeEnd = maxValue
      
        // Add next element from same list
        if index + 1 < lists[listIndex].length:
            nextValue = lists[listIndex][index + 1]
            minHeap.add((nextValue, index + 1, listIndex))
            maxValue = max(maxValue, nextValue)
  
    return [rangeStart, rangeEnd]
```

### Time Complexity: O(n log k) where n is total elements

### Space Complexity: O(k)

### Practice Problems

1. **Kth Smallest in Sorted Matrix**: Find kth smallest in n×n matrix
2. **Merge Sorted Arrays**: Merge multiple sorted arrays
3. **Find K Pairs with Smallest Sums**: From two arrays

---

## 16. Topological Sort

### Description

Linear ordering of vertices in directed graph where vertex u comes before vertex v for every directed edge u→v. Used for dependency resolution.

### When to Use

- **Task scheduling**: With dependencies
- **Course prerequisites**: Academic planning
- **Build systems**: Dependency resolution
- **Cycle detection**: In directed graphs

### Strategy

1. **Kahn's Algorithm**: Use in-degree count

   - Find nodes with in-degree 0
   - Remove them and update in-degrees
   - Repeat until all processed
2. **DFS-based**: Use recursion

   - Perform DFS and add to result on completion
   - Reverse the result

### Example Problem: Topological Sort

**Problem**: Find topological ordering of vertices.

**Pseudocode (Kahn's Algorithm)**:

```
function topologicalSort(vertices, edges):
    // Build graph and calculate in-degrees
    graph = {}
    inDegree = {}
  
    for i = 0 to vertices-1:
        graph[i] = []
        inDegree[i] = 0
  
    for edge in edges:
        source, destination = edge
        graph[source].add(destination)
        inDegree[destination]++
  
    // Find sources (vertices with 0 in-degree)
    queue = []
    for vertex in inDegree:
        if inDegree[vertex] == 0:
            queue.add(vertex)
  
    result = []
    while not queue.isEmpty():
        vertex = queue.remove()
        result.add(vertex)
      
        // Update in-degrees of neighbors
        for neighbor in graph[vertex]:
            inDegree[neighbor]--
            if inDegree[neighbor] == 0:
                queue.add(neighbor)
  
    // Check for cycle
    if result.length != vertices:
        return []  // Cycle detected
  
    return result
```

### Course Schedule Example:

```
function canFinishCourses(numCourses, prerequisites):
    // Same as topological sort
    graph = build_graph(numCourses, prerequisites)
    inDegree = calculate_in_degrees(graph)
  
    queue = find_sources(inDegree)
    processedCourses = 0
  
    while not queue.isEmpty():
        course = queue.remove()
        processedCourses++
      
        for neighbor in graph[course]:
            inDegree[neighbor]--
            if inDegree[neighbor] == 0:
                queue.add(neighbor)
  
    return processedCourses == numCourses
```

### DFS-based Topological Sort:

```
function topologicalSortDFS(vertices, edges):
    graph = build_graph(vertices, edges)
    visited = {}
    result = []
  
    for vertex = 0 to vertices-1:
        if vertex not in visited:
            dfs(vertex, graph, visited, result)
  
    return reverse(result)

function dfs(vertex, graph, visited, result):
    visited[vertex] = true
  
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(neighbor, graph, visited, result)
  
    result.add(vertex)  // Add after processing children
```

### Time Complexity: O(V + E)

### Space Complexity: O(V + E)

### Practice Problems

1. **Course Schedule**: Check if all courses can be finished
2. **Course Schedule II**: Find valid course order
3. **Alien Dictionary**: Derive character order from sorted words

---

## 17. Trie

### Description

Tree-like data structure for storing strings where each node represents a character. Efficient for prefix-based operations and string searching.

### When to Use

- **Autocomplete**: Suggesting completions
- **Spell checkers**: Word validation
- **IP routing**: Longest prefix matching
- **Word games**: Boggle, word search

### Strategy

1. Each node contains children for possible next characters
2. Mark end of word with special flag
3. Traverse from root following character path
4. Support insertion, search, and prefix operations

### Example Problem: Implement Trie

**Problem**: Implement insert, search, and startsWith operations.

**Pseudocode**:

```
class TrieNode:
    function __init__():
        children = {}  // Map character to TrieNode
        isEndOfWord = false

class Trie:
    function __init__():
        root = TrieNode()
  
    function insert(word):
        current = root
      
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
      
        current.isEndOfWord = true
  
    function search(word):
        current = root
      
        for char in word:
            if char not in current.children:
                return false
            current = current.children[char]
      
        return current.isEndOfWord
  
    function startsWith(prefix):
        current = root
      
        for char in prefix:
            if char not in current.children:
                return false
            current = current.children[char]
      
        return true
```

### Word Search in Grid Example:

```
function wordSearch(board, word):
    trie = Trie()
    trie.insert(word)
  
    for i = 0 to board.length-1:
        for j = 0 to board[0].length-1:
            if dfsSearch(board, i, j, trie.root, word, 0):
                return true
  
    return false

function dfsSearch(board, row, col, node, word, index):
    if index == word.length:
        return node.isEndOfWord
  
    if row < 0 or row >= board.length or col < 0 or col >= board[0].length:
        return false
  
    char = board[row][col]
    if char not in node.children:
        return false
  
    board[row][col] = '#'  // Mark as visited
  
    found = dfsSearch(board, row-1, col, node.children[char], word, index+1) or
            dfsSearch(board, row+1, col, node.children[char], word, index+1) or
            dfsSearch(board, row, col-1, node.children[char], word, index+1) or
            dfsSearch(board, row, col+1, node.children[char], word, index+1)
  
    board[row][col] = char  // Restore
    return found
```

### Auto-complete Example:

```
function autoComplete(prefix):
    current = root
  
    // Navigate to prefix end
    for char in prefix:
        if char not in current.children:
            return []
        current = current.children[char]
  
    // Collect all words with this prefix
    words = []
    collectWords(current, prefix, words)
    return words

function collectWords(node, currentWord, words):
    if node.isEndOfWord:
        words.add(currentWord)
  
    for char in node.children:
        collectWords(node.children[char], currentWord + char, words)
```

### Time Complexity: O(m) for insert/search where m is word length

### Space Complexity: O(ALPHABET_SIZE × N × M) worst case

### Practice Problems

1. **Word Search II**: Find all words in board
2. **Design Add and Search Words**: With wildcard support
3. **Replace Words**: Replace words with roots

---

## 18. Backtracking

### Description

Explores all possible solutions by making choices, and undoing them if they don't lead to a solution. Systematic way to explore solution space.

### When to Use

- **Combinatorial optimization**: Finding optimal combinations
- **Puzzle solving**: Sudoku, N-Queens, crosswords
- **Path finding**: With constraints
- **Generate all solutions**: Permutations, combinations

### Strategy

1. **Choose**: Make a choice from available options
2. **Explore**: Recursively explore with this choice
3. **Unchoose**: Backtrack if choice doesn't work
4. **Base case**: Solution found or no more choices

### Example Problem: N-Queens

**Problem**: Place N queens on N×N board so no two queens attack each other.

**Pseudocode**:

```
function solveNQueens(n):
    board = createEmptyBoard(n)
    solutions = []
    placeQueens(board, 0, solutions)
    return solutions

function placeQueens(board, row, solutions):
    if row == board.length:
        solutions.add(board.copy())
        return
  
    for col = 0 to board.length-1:
        if isSafe(board, row, col):
            // Choose
            board[row][col] = 'Q'
          
            // Explore
            placeQueens(board, row + 1, solutions)
          
            // Unchoose (backtrack)
            board[row][col] = '.'

function isSafe(board, row, col):
    // Check column
    for i = 0 to row-1:
        if board[i][col] == 'Q':
            return false
  
    // Check diagonals
    for i = row-1, j = col-1; i >= 0 and j >= 0; i--, j--:
        if board[i][j] == 'Q':
            return false
  
    for i = row-1, j = col+1; i >= 0 and j < board.length; i--, j++:
        if board[i][j] == 'Q':
            return false
  
    return true
```

### Sudoku Solver Example:

```
function solveSudoku(board):
    return backtrackSudoku(board)

function backtrackSudoku(board):
    for row = 0 to 8:
        for col = 0 to 8:
            if board[row][col] == '.':
                for digit = '1' to '9':
                    if isValidSudoku(board, row, col, digit):
                        // Choose
                        board[row][col] = digit
                      
                        // Explore
                        if backtrackSudoku(board):
                            return true
                      
                        // Unchoose
                        board[row][col] = '.'
              
                return false  // No valid digit found
  
    return true  // All cells filled

function isValidSudoku(board, row, col, digit):
    // Check row, column, and 3x3 box
    for i = 0 to 8:
        if board[row][i] == digit or board[i][col] == digit:
            return false
  
    startRow = (row / 3) * 3
    startCol = (col / 3) * 3
    for i = startRow to startRow+2:
        for j = startCol to startCol+2:
            if board[i][j] == digit:
                return false
  
    return true
```

### Word Break Example:

```
function wordBreak(s, wordDict):
    return backtrackWordBreak(s, 0, wordDict, {})

function backtrackWordBreak(s, start, wordDict, memo):
    if start == s.length:
        return true
  
    if start in memo:
        return memo[start]
  
    for end = start+1 to s.length:
        word = s[start:end]
        if word in wordDict and backtrackWordBreak(s, end, wordDict, memo):
            memo[start] = true
            return true
  
    memo[start] = false
    return false
```

### Time Complexity: Exponential in worst case

### Space Complexity: O(depth) for recursion stack

### Practice Problems

1. **Generate Parentheses**: All valid parentheses combinations
2. **Letter Combinations**: Of phone number
3. **Palindrome Partitioning**: All palindrome partitions

---

## 19. Monotonic Stack

### Description

Stack that maintains elements in monotonic (increasing or decreasing) order. Elements violating the order are removed before insertion.

### When to Use

- **Next greater/smaller element**: In array
- **Histogram problems**: Maximum rectangle area
- **Temperature problems**: Warmer day finding
- **Stock span**: Days when price was lower

### Strategy

1. **Monotonic Increasing**: Remove elements from top while stack top > current
2. **Monotonic Decreasing**: Remove elements from top while stack top < current
3. Use stack to track indices or values
4. Process remaining elements for final answer

### Example Problem: Next Greater Element

**Problem**: Find next greater element for each element in array.

**Pseudocode**:

```
function nextGreaterElements(nums):
    result = array of size nums.length filled with -1
    stack = []  // Monotonic decreasing stack (indices)
  
    for i = 0 to nums.length-1:
        // Remove elements smaller than current
        while not stack.isEmpty() and nums[stack.top()] < nums[i]:
            index = stack.pop()
            result[index] = nums[i]
      
        stack.push(i)
  
    return result
```

### Daily Temperatures Example:

```
function dailyTemperatures(temperatures):
    result = array of size temperatures.length filled with 0
    stack = []  // Store indices
  
    for i = 0 to temperatures.length-1:
        while not stack.isEmpty() and temperatures[stack.top()] < temperatures[i]:
            index = stack.pop()
            result[index] = i - index  // Days to wait
      
        stack.push(i)
  
    return result
```

### Largest Rectangle in Histogram:

```
function largestRectangleArea(heights):
    stack = []  // Monotonic increasing stack (indices)
    maxArea = 0
  
    for i = 0 to heights.length-1:
        while not stack.isEmpty() and heights[stack.top()] > heights[i]:
            height = heights[stack.pop()]
            width = stack.isEmpty() ? i : i - stack.top() - 1
            maxArea = max(maxArea, height * width)
      
        stack.push(i)
  
    // Process remaining elements
    while not stack.isEmpty():
        height = heights[stack.pop()]
        width = stack.isEmpty() ? heights.length : heights.length - stack.top() - 1
        maxArea = max(maxArea, height * width)
  
    return maxArea
```

### Sliding Window Maximum:

```
function maxSlidingWindow(nums, k):
    result = []
    deque = []  // Store indices in decreasing order of values
  
    for i = 0 to nums.length-1:
        // Remove indices outside window
        while not deque.isEmpty() and deque.front() <= i - k:
            deque.removeFront()
      
        // Remove smaller elements
        while not deque.isEmpty() and nums[deque.back()] < nums[i]:
            deque.removeBack()
      
        deque.addBack(i)
      
        if i >= k - 1:
            result.add(nums[deque.front()])
  
    return result
```

### Time Complexity: O(n)

### Space Complexity: O(n)

### Practice Problems

1. **Remove K Digits**: To make smallest number
2. **Trapping Rain Water**: Calculate trapped water
3. **Sum of Subarray Minimums**: Sum of minimum in all subarrays

---

## 20. 0/1 Knapsack (Dynamic Programming)

### Description

Classic optimization problem where items have weight and value, and goal is to maximize value within weight capacity. Each item can be taken once (0/1).

### When to Use

- **Resource allocation**: Limited capacity optimization
- **Budget problems**: Maximize return with budget constraint
- **Subset selection**: With weight/capacity constraints
- **Optimization problems**: With binary choices

### Strategy

1. **Bottom-up DP**: Build table dp[i][w] = max value using first i items with weight ≤ w
2. **Top-down DP**: Recursion with memoization
3. **Space optimization**: Use 1D array since only previous row needed

### Example Problem: 0/1 Knapsack

**Problem**: Maximum value achievable with weight capacity C.

**Pseudocode (Bottom-up)**:

```
function knapsack(weights, values, capacity):
    n = weights.length
    // dp[i][w] = max value using items 0 to i-1 with capacity w
    dp = 2D array of size (n+1) x (capacity+1)
  
    // Initialize base cases
    for i = 0 to n:
        dp[i][0] = 0
    for w = 0 to capacity:
        dp[0][w] = 0
  
    for i = 1 to n:
        for w = 1 to capacity:
            // Don't include current item
            dp[i][w] = dp[i-1][w]
          
            // Include current item if possible
            if weights[i-1] <= w:
                includeValue = values[i-1] + dp[i-1][w - weights[i-1]]
                dp[i][w] = max(dp[i][w], includeValue)
  
    return dp[n][capacity]
```

### Space-Optimized Version:

```
function knapsackOptimized(weights, values, capacity):
    dp = array of size (capacity + 1) filled with 0
  
    for i = 0 to weights.length-1:
        // Traverse from right to left to avoid using updated values
        for w = capacity down to weights[i]:
            dp[w] = max(dp[w], values[i] + dp[w - weights[i]])
  
    return dp[capacity]
```

### Equal Subset Sum Partition:

```
function canPartition(nums):
    totalSum = sum(nums)
  
    if totalSum % 2 != 0:
        return false
  
    target = totalSum / 2
    dp = array of size (target + 1) filled with false
    dp[0] = true
  
    for num in nums:
        for sum = target down to num:
            dp[sum] = dp[sum] or dp[sum - num]
  
    return dp[target]
```

### Subset Sum Example:

```
function subsetSum(nums, target):
    dp = array of size (target + 1) filled with false
    dp[0] = true
  
    for num in nums:
        for sum = target down to num:
            dp[sum] = dp[sum] or dp[sum - num]
  
    return dp[target]
```

### Count of Subset Sum:

```
function countSubsetSum(nums, target):
    dp = array of size (target + 1) filled with 0
    dp[0] = 1
  
    for num in nums:
        for sum = target down to num:
            dp[sum] += dp[sum - num]
  
    return dp[target]
```

### Time Complexity: O(n × capacity)

### Space Complexity: O(capacity) with optimization

### Practice Problems

1. **Target Sum**: Assign +/- to reach target
2. **Minimum Subset Sum Difference**: Minimize difference between subsets
3. **Count of Subset Sum**: Number of ways to achieve target sum

---

## Summary and Practice Strategy

### Pattern Recognition Tips

1. **Array problems with two elements**: Consider Two Pointers
2. **Linked list cycles**: Use Fast & Slow Pointers
3. **Contiguous subarrays**: Apply Sliding Window
4. **Tree level-order problems**: Use BFS
5. **Path-related tree problems**: Use DFS
6. **Top K problems**: Use Heaps
7. **Overlapping intervals**: Use Merge Intervals
8. **Recursive exploration**: Apply Backtracking

### Practice Approach

1. **Start with pattern identification**: Read problem and identify which pattern applies
2. **Understand the template**: Master the basic template for each pattern
3. **Practice variations**: Solve multiple problems using same pattern
4. **Combine patterns**: Advanced problems often use multiple patterns
5. **Time yourself**: Practice under interview conditions

### Common Mistakes to Avoid

1. **Off-by-one errors**: Especially in array indexing
2. **Infinite loops**: In while loops with pointers
3. **Memory leaks**: In tree/graph problems
4. **Edge cases**: Empty inputs, single elements
5. **Integer overflow**: In sum calculations

Remember: **Practice consistently and focus on understanding the underlying principles rather than memorizing solutions.**
