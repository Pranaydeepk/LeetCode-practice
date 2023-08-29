class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        result, count = nums[0], 1
        for i in range(1, len(nums)):
            if nums[i] == result:
                count += 1
            else:
                count -= 1
            if count == 0:
                result = nums[i+1]
        return result