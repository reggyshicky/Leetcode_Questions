//find the maximum number
let nums = [10, 8, 86, 78, 2, -1000]

//first alternative
console.log("Math.max option", Math.max(...nums))

//second alternative
let num = -Infinity //this is the lowest lowest number
for (let i = 0; i < nums.length; nums++) {
    if (nums[i] > num) {
        num = nums[i]
    }
}
console.log("max number", num)



