// best solution - quicksort style
var rotate = function(nums, k) {
    let iter
    k = k % nums.length
    while (k > 0) {
        iter = nums.length-1
        last = nums[iter]
        while (iter > 0) {
            nums[iter] = nums[--iter]
        }
        nums[0] = last
        k--
    }
    return nums
};

console.log(rotate())