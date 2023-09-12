class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        esum,n = 0, len(nums)
        dsum = 0
        esum = sum(nums)
        for num in nums:
            while num:
                dsum += num%10
                num = num//10
        return abs(esum-dsum)        