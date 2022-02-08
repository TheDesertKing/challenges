/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    for (let i = 1; i < nums.length; i++) {
        while(nums[i] == nums[i - 1]) {
            nums.splice(i,1)
        }
    }
    return nums.length,nums
};

const t1 = [1,1,1,2,3,4,4,5,6,6,6]
const s1 = removeDuplicates(t1)

s1