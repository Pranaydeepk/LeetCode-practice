class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        answer = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j != i and nums[j] < nums[i]:
                    answer[i] += 1
        return answer