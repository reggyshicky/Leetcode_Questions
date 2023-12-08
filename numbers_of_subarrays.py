'''
Given an array of positive integers nums and an integer k, return the number of subarrays where the product of all the elements in the subarray is strictly less than k.

For example, given the input nums = [10, 5, 2, 6], k = 100, the answer is 8. The subarrays with products less than k are:

[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
'''
from typing import List
def numSubarrayProductLessThanK(num: List[int], k:int):
    currProduct = 1
    left = 0
    ansArr = 0
    
    if k <= 1: #our aim to get arrays with product less than k , if k is 1 , then it means we are looking at product 0, we cannot have at any given a product 0
        return 0
    
    for right in range(len(num)):
        currProduct *= num[right]
        
        while currProduct >= k:
            currProduct //= num[left]
            left += 1
            
        ansArr = ansArr + right - left + 1
        
    return ansArr
    
    
print(numSubarrayProductLessThanK([10, 5, 2, 6], 100))