class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        integer = set()
        for i in nums:
            for point in range(i[0],i[1]+1):
                integer.add(point)
        return len(integer)