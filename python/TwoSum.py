class solution:
    def TwoSum(self, nums, target):
        hashmap = {}
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in hashmap:
                return [i, hashmap[compliment]]
            hashmap[nums[i]] = i

instance = solution()
print(instance.TwoSum([2,7,11,15], 9))
