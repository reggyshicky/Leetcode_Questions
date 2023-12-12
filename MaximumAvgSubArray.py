# You are given an integer array nums consisting of n elements, and an integer k.
# Find a contiguous subarray whose length is equal to k that has the maximum average
# value and return this value. Any answer with a calculation error less than 10-5 will be accepted.
import typing
def findMaxAverage(nums: typing.List[int], k: int):
    currAvg = 0
    ans = 0
    currSum = 0
    for i in range(k):
        currSum  = currSum + nums[i]
        currAvg = currSum / k
    
    ans = currAvg
    
    for j in range(k, len(nums)):
        currSum = currSum + nums[j] - nums[j - k]
        currAvg = currSum / k
        
        ans = max(ans, currAvg)
        
    return ans
        
print(findMaxAverage([1,12,-5,-6,50,3], 4))  
        
        