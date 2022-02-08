/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    let first = 0
    let second = 1
    let len = nums.length
    while (second < nums.length) {
        if (nums[first] == nums[second]) {
            len--
            second++
        }
        else {
            nums[++first] = nums[second++]
        }
    }
    return [len,...nums]
};

let t1 =[1,2,3,3,4,4,5,6,7,7,7,8,8,9]
let t2 =[1,2,3,3,4,4]
let t3 =[1,2,3,3,4,4,5,5,5,6]
let t4 = [1,2,2,2,4,4,4,5,6]

// console.log(t2)
// console.log(removeDuplicates(t2))
// console.log(t1)
// console.log(removeDuplicates(t1))
// console.log(t3)
// console.log(removeDuplicates(t3))
console.log(t4)
console.log(removeDuplicates(t4))