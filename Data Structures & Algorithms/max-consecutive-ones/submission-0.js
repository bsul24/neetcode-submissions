class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    findMaxConsecutiveOnes(nums) {
        let max = 0;
        let cur = 0
        for (let i = 0; i < nums.length; i++) {
            if (nums[i] === 1) {
                cur++
                if (cur > max) {
                    max = cur
                }
            } else {
                cur = 0
            }
        }
        return max
    }
}
