class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # count = 0
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if nums[i] == nums[j]:
        #             count += 1
        # return count
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        count = 0
        for x,y in freq.items():
            count += y*(y-1)/2
        return int(count)