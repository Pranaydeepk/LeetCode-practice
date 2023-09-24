class Solution:
    def rob(self, nums: List[int]) -> int:
        # rob1, rob2 = 0, 0
        # for rob in nums:
        #     curr = max(rob1 + rob, rob2)
        #     rob1 = rob2
        #     rob2 = curr
        # return rob2
        for i in range(1,len(nums)):
            if i == 1:
                nums[i] = max(nums[i], nums[i-1])
            else:
                nums[i] = max(nums[i-2] + nums[i], nums[i-1])
        return nums[-1]