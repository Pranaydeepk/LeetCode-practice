class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        def countSetBits(n):
            count = 0
            while (n):
                count += n & 1
                n >>= 1
            return count
        total = 0
        for i in range(len(nums)):
            if countSetBits(i) == k:
                total += nums[i]
        return total