class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        result = []
        v = 0
        p = 0
        s = 0
        for i in range(len(nums)):
            p = len(set(nums[0:i+1]))
            s = len(set(nums[i+1:]))
            v = p - s
            result.append(v)
        return result