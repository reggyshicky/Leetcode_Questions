"""
You are given a 0-indexed array nums of n integers, and an integer k.
The k-radius average for a subarray of nums centered at some index i 
with the radius k is the average of all elements in nums between the 
indices i - k and i + k (inclusive). If there are less than k elements 
before or after the index i, then the k-radius average is -1.
Build and return an array avgs of length n where avgs[i] is the k-radius 
average for the subarray centered at index i.
"""
import typing
def getAverages(nums: typing.List[int], k: int) -> typing.List[int]:
    n = len(nums)
    avgs = [-1] * n
    left = 0
    window_sum = 0
    diameter = 2 * k + 1
    
    for right in range(n):
        window_sum += nums[right]
        
        if right - left + 1 == diameter:
            avgs[left + k] = window_sum // diameter
            # left+k gets the center index of the current window
            window_sum -= nums[left]
            left += 1
    return avgs
    
res = getAverages([7,4,3,9,1,8,5,2,6], 3)
print(res)
