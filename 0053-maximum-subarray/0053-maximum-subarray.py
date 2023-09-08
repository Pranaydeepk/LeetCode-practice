class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = nums[0]
        maxcurr = nums[0]
        for i in range(1,len(nums)):
            maxcurr = max(maxcurr+nums[i],nums[i])
            maxsum = max(maxsum,maxcurr)
        return maxsum
        