class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hs = {}
        for i in nums:
            if i in hs:
                hs[i] += 1
                if hs[i] == 2:
                    return True
            hs[i] = 1
        return False