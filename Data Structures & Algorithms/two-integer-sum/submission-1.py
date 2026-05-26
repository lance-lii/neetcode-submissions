class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} 
        for i in range(len(nums)):
            x = nums[i]
            needed = target - x
            if needed in seen:
                j = seen[needed]
                return [j, i] if j < i else [i, j]
            seen[x]=i