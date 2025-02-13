let arr = [1,2,3,4,5,6, 7]
let x = 0
let y = arr.length - 1
console.log(y)

//odd Number length of an array
while(x <= y) {
    console.log(`Array at position ${x} ${arr[x]}, Array at position ${y} ${arr[y]}`)
    if (x === y) {
        console.log("the mid values is", arr[y])
    }
    x++;
    y--;
}

//Even number length of an array
console.log("-----------------------------------------")
let arr2 = [1,2,3,4,5,6]
let left = 0
let right = arr2.length - 1
while(left < right) {
    console.log(`Array at position ${left} ${arr2[left]}, Array at position ${right} ${arr2[right]}`)
    if (left === right) {
        console.log("the mid values is", arr2[right])
    }
    
    //if (right - left === 1) this condition is also correct, always return the left
    if (Number(left) + 1 === right) {
        console.log("medium", arr2[left])
    }
    left++;
    right--;
}

//Note: for an even array, half of the array is floored(less index by 1) and half of the other array is sealed(more indexes by one)
