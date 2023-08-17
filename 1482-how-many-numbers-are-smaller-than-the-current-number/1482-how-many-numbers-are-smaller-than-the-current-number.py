class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        answer = []
        freq = {}
        temp = sorted(nums)
        for i in range(len(temp)):
            if temp[i] not in freq:
                freq[temp[i]] = i
        for i in range(len(nums)):
            answer.append(freq[nums[i]])
        return answer