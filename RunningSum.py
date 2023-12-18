#Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

#Return the running sum of nums.
import typing
def runningSum(nums: typing.List[int]) -> typing.List[int]:
    prefix = [nums[0]]
    
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[i - 1])
    return prefix

print(runningSum([[1,2,3,4]]))