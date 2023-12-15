/*
Given an integer array nums, find the number of ways to split the array into two parts so that the first section has a sum greater 
than or equal to the sum of the second section. The second section should have at least one number.
*/

function waysToSplitArray(nums) {
    let n = nums.length;
    let prefix = [nums[0]];
    let ansArr = 0;

    for (let i = 1; i < n; i++) {
        prefix.push(nums[i] + prefix[i - 1]);
    }

    for (let j = 0; j < (n - 1); j++) {
        let left_section = prefix[j]
        let right_section = prefix[n - 1] - prefix[j];

        if (left_section >= right_section) {
            ansArr = ansArr + 1;
        }

    }
    return ansArr;
}

console.log(waysToSplitArray([10, 4, -8, 7]));