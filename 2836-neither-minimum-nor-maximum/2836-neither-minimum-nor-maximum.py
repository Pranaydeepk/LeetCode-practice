class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return -1
        least, highest = min(nums), max(nums)
        for i in nums:
            if i != least and i != highest:
                return i