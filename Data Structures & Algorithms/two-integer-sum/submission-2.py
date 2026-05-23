class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        nums_set = set(nums)

        for i in range(len(nums)):
            search = target - nums[i]
            if search in nums_set:
                for j in range(i+1, len(nums)):
                    if nums[j] == search:
                        return [i, j]

