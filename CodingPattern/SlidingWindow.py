"""
@author : Ajeet Kumar
@webpage : https://www.ajeetkbhardwaj.github.io

Coding Pattern : Sliding Window 
used to solve problems that involve a contiguous subarray or linkedlist within a larger array or linkedlist.

problem-1 : 
@leetcode : https://leetcode.com/problems/maximum-average-subarray-i/

@statement : Given an array, find the average of all contiguous subarrays of size K in it.

problem-2 : 
@leetcode : https://leetcode.com/problems/largest-subarray-length-k/

@statement : Given an array of positive numbers and a positive number K, find the maximum sum of any contiguous subarray of size K.


problem-3 : 
@leetcode : https://leetcode.com/problems/minimum-size-subarray-sum/

@statement : Given an array of positive numbers and a positive number S, find the length of the smallest contiguous subarray whose sum is greater than or equal to S.
Return 0 if no such subarray exists.

problem-4 : 
@leetcode : https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
statement : Given a string, find the length of the longest substring in it with no more than K distinct characters.
You can assume that K is less than or equal to the length of the given string.

problem-5 :
leetcode :https://leetcode.com/problems/fruit-into-baskets/
statement :Given an array of characters where each character represents a fruit tree, you are given two baskets, and your goal is to put the maximum number of fruits in each basket. The only restriction is that each basket can have only one type of fruit.
You can start with any tree, but you cant skip a tree once you have started. You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.
Write a function to return the maximum number of fruits in both baskets.


"""


# 1.0 Brute Force Approach
def find_avg_of_subarrays(arr, K):
    n = len(arr)
    result = []
    for i in range(n - K + 1):
        subarray_sum = 0
        for j in range(i, i + K):
            subarray_sum += arr[j]
        result.append(subarray_sum / K)
    return result

# 1.1 Sliding Window Approach
def find_avg_of_subarrays_sliding_window(arr, K):
    n = len(arr)
    result = []
    window_sum = 0
    window_start = 0

    for window_end in range(n):
        window_sum += arr[window_end]  # Add the next element to the window
        
        # Slide the window, we have hit the size of K
        if window_end >= K - 1:
            result.append(window_sum / K)  # Calculate the average
            window_sum -= arr[window_start]  # Subtract the element going out of the window
            window_start += 1  # Slide the window ahead

    return result

# 2.0 Brute Force Approach
def largest_subarray_length_k(arr, K):
    n = len(arr)
    max_sum = float('-inf')
    for i in range(n - K + 1):
        subarray_sum = 0
        for j in range(i, i + K):
            subarray_sum += arr[j]
        max_sum = max(max_sum, subarray_sum)
    return max_sum

# 2.1 Sliding Window Approach
def largest_subarray_length_k(arr, K):
    n = len(arr)
    max_sum = float('-inf')
    window_sum = 0
    window_start = 0

    for window_end in range(n):
        window_sum += arr[window_end]  # Add the next element to the window
        
        # Slide the window, we have hit the size of K
        if window_end >= K - 1:
            max_sum = max(max_sum, window_sum)  # Update max sum if needed
            window_sum -= arr[window_start]  # Subtract the element going out of the window
            window_start += 1  # Slide the window ahead

    return max_sum

# 3.0 Brute Force Approach
def min_size_subarray_sum(arr, S):
    n = len(arr)
    min_length = float('inf')
    
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += arr[j]
            if current_sum >= S:
                min_length = min(min_length, j - i + 1)
                break  # No need to check further for this starting point

    return min_length if min_length != float('inf') else 0

# 3.1 Sliding Window Approach
def min_size_subarray_sum_sliding_window(arr, S):
    n = len(arr)
    min_length = float('inf')
    window_sum = 0
    window_start = 0

    for window_end in range(n):
        window_sum += arr[window_end]  # Add the next element to the window
        
        # Shrink the window as small as possible while the sum is greater than or equal to S
        while window_sum >= S:
            min_length = min(min_length, window_end - window_start + 1)
            window_sum -= arr[window_start]  # Subtract the element going out of the window
            window_start += 1  # Slide the window ahead

    return min_length if min_length != float('inf') else 0


# 4.0 Brute Force Approach
def longest_substring_k_distinct(s, K):
    n = len(s)
    max_length = 0
    
    for i in range(n):
        char_count = {}
        distinct_count = 0
        
        for j in range(i, n):
            if s[j] not in char_count:
                char_count[s[j]] = 0
                distinct_count += 1
            char_count[s[j]] += 1
            
            if distinct_count > K:
                break
            
            max_length = max(max_length, j - i + 1)

    return max_length

# 4.1 Sliding Window Approach
def longest_substring_k_distinct_sliding_window(s, K):
    n = len(s)
    max_length = 0
    char_count = {}
    window_start = 0

    for window_end in range(n):
        if s[window_end] not in char_count:
            char_count[s[window_end]] = 0
        char_count[s[window_end]] += 1
        
        # Shrink the window if we have more than K distinct characters
        while len(char_count) > K:
            char_count[s[window_start]] -= 1
            if char_count[s[window_start]] == 0:
                del char_count[s[window_start]]
            window_start += 1
        
        max_length = max(max_length, window_end - window_start + 1)

    return max_length

# 5.0 Brute Force Approach
def max_fruits_in_baskets(fruits):
    n = len(fruits)
    max_fruits = 0
    
    for i in range(n):
        fruit_count = {}
        for j in range(i, n):
            if fruits[j] not in fruit_count:
                fruit_count[fruits[j]] = 0
            fruit_count[fruits[j]] += 1
            
            if len(fruit_count) > 2:  # More than two types of fruits
                break
            
            max_fruits = max(max_fruits, j - i + 1)

    return max_fruits

# 5.1 Sliding Window Approach
def max_fruits_in_baskets_sliding_window(fruits):
    n = len(fruits)
    max_fruits = 0
    fruit_count = {}
    window_start = 0

    for window_end in range(n):
        if fruits[window_end] not in fruit_count:
            fruit_count[fruits[window_end]] = 0
        fruit_count[fruits[window_end]] += 1
        
        # Shrink the window if we have more than 2 types of fruits
        while len(fruit_count) > 2:
            fruit_count[fruits[window_start]] -= 1
            if fruit_count[fruits[window_start]] == 0:
                del fruit_count[fruits[window_start]]
            window_start += 1
        
        max_fruits = max(max_fruits, window_end - window_start + 1)

    return max_fruits