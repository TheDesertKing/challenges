// two arrays solution
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function(nums, k) {
    k = k % nums.length
    let a = nums.slice(nums.length-k)
    nums.splice(nums.length-k,k)
    nums.unshift(...a)
    return nums
};
let k = [1,2,3,4,5]
console.log(rotate(k,3))
console.log(k.slice(2))