'''
Longest_SubArray.pyGiven an array of positive integers nums and an integer k, 
find the length of the longest subarray whose sum is less than or equal to k. 
This is the problem we have been talking about above. We will now formally solve it.
'''
from typing import List

def find_length(nums: List[int], k: int) -> int:
    currSum = 0
    left = 0
    ansArray = 0
    
    for right in range(len(nums)):
        currSum += nums[right]
        
        while currSum > k:
            currSum -= nums[left]
            left += 1
        ansArray = max(ansArray, (right - left + 1))
    return ansArray

arr = [3, 1, 2, 7, 4, 2, 1, 1, 5]
k = 8.
print(find_length(arr, k))
      