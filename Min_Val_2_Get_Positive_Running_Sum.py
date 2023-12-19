"""
Given an array of integers nums, you start with an initial positive 
value startValue. In each iteration, you calculate the step by step 
sum of startValue plus elements in nums (from left to right).
Return the minimum positive value of startValue such that the 
step by step sum is never less than 1.
tip: "First find the minimum prefix sum"
"""
import typing


def minStartValue(nums: typing.List[int]) -> int:
    prefix = [nums[0]]
    startValue = 0
    minPrefixSum = 0
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[i - 1])
    minPrefixSum = min(prefix)
    
    if minPrefixSum < 1:
        startValue = 1 - minPrefixSum # mathematically minPrefixSum + y  = 1 find y
    else:
        startValue = 1
        
    return startValue

print(minStartValue([-3,2,-3,4,2]))
# ans is 
        
         
        
        
    