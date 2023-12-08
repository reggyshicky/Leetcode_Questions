//Given an integer array nums and an integer k, 
//find the sum of the subarray with the largest sum whose length is k.

function find_best_subarray (nums, k) {
    let currSum = 0;
    let ans = 0;

    for (let i = 0; i < k; i++) {
        currSum += nums[i];
    }
    ans = currSum;

    for (let j = k; j < nums.length; j++) {
        currSum = currSum + nums[j] - nums[j - k];
        ans = Math.max(ans, currSum);
    }
    return ans;
}

console.log(find_best_subarray([3, -1, 4, 12, -8, 5, 6], 4))
