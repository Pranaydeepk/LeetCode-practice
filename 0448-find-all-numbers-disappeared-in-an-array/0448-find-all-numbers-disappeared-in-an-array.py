class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        d = {}
        for i in range(1,len(nums)+1):
            if i not in d:
                d[i] = 0
        for i in nums:
            if i in d:
                d[i] += 1
        result = []
        for x,y in d.items():
            if y == 0:
                result.append(x)
        return result