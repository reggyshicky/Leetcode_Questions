//Find the maximum length of the a subarray/window

function Find_Length(arr, target) {
    currSum = 0;
    ansArr = 0;
    left = 0;
    
    for (let right = 0; right < arr.length; right++) {
        currSum += arr[right];

        while (currSum > target) {
            currSum -= arr[left];
            left += 1;
        }
        ansArr = Math.max(ansArr, right - left + 1)
    }
    return ansArr;
}

console.log(Find_Length([3, 1, 2, 7, 4, 2, 1, 1, 5], 8));