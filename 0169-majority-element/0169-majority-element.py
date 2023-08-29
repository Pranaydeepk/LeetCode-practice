class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # nums.sort()
        # return nums[len(nums)//2]
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]] += 1
                continue
            d[nums[i]] = 1
        for i in d:
            if d[i] > len(nums)//2:
                return i
        # return 0





# 1 1 1 1 7 9 9 90
# 1 2 3 4 5 5 5 5 