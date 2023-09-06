class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pivotIdx = -1
        leftsum = 0
        totalsum = sum(nums)
        for i in range(len(nums)):
            if leftsum == totalsum - leftsum - nums[i]:
                pivotIdx = i
                break
            leftsum += nums[i]
        return pivotIdx