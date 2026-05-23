class Solution {
    /**
     * @param {number[]} nums
     * @param {number} val
     * @return {number}
     */
    removeElement(nums, val) {
        let total = 0
        let cur = 0
        for (const num of nums) {
            if (num !== val) {
                nums[cur] = num
                cur++
                total++
            }
        }
        return total
    }
}
