/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    //going backwards so i solve where first accurance stays.
    for (let i = nums.length-1; i > 0; i--) {
        if (nums.indexOf(nums[i]) != i) {
            nums.splice(i,1)
        }
    }
    return [nums.length,nums]
};



let test1=  [3,2,3,4,5,6,8,7]
let test2=[1,2,1,4,1,2,3,1,1,2,1 ]
let test3 = [1,1,2]

const s1 = removeDuplicates(test1)
let s2 = removeDuplicates(test2)
let s3 = removeDuplicates(test3)

s1
s2
s3