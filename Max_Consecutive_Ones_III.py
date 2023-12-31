#given a binary array nums and an integer k, return the maximum number of 
# consecutive 1's in the array if you can flip at most k 0's.
# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
#Output: 6
#Explanation: [1,1,1,0,0,1,1,1,1,1,1]
#Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
import typing
def longestOnes(nums: typing.List[int], k: int) -> int:
    left = 0
    currNoZeros = 0
    ansArr = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            currNoZeros += 1
            
        while (currNoZeros > k):
            if nums[left] == 0:
                currNoZeros -= 1
            left += 1
            
            ansArr = max(ansArr, right - left + 1)
    return ansArr

print(longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))
print(longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))