"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


"""

def two_sum(array, target):
    """
    Function to find indices of the two numbers such that they add up to target.
    
    :param array: List[int] - List of integers
    :param target: int - Target sum
    :return: List[int] - Indices of the two numbers
    """
    # Dictionary to store the numbers and their indices
    num_to_index = {}
    
    # Iterate through the array
    for index, num in enumerate(array):
        # Calculate the complement that would sum to the target
        complement = target - num
        # If the complement exists in the dictionary, return the indices
        if complement in num_to_index:
            return [num_to_index[complement], index]
        # Otherwise, store the number and its index in the dictionary
        num_to_index[num] = index
    
    return []  # Return an empty list if no solution is found

# Example usage
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 18
    result = two_sum(nums, target)
    print(f"Indices of the two numbers that add up to {target}: {result}")
