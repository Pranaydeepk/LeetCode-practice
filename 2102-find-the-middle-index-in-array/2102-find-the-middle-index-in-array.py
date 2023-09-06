class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        totalsum, leftsum = sum(nums), 0
        for i in range(len(nums)):
            if leftsum == totalsum - nums[i] - leftsum:
                return i
            leftsum += nums[i]
        return -1
        