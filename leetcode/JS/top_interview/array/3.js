// going for the o(1) space solution
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function(nums, k) {
    while (k > 0) {
        nums.unshift(nums.pop())
        k--
    }
    return nums
};

let t1 = [1,2,3,4]
console.log(rotate(t1,2))