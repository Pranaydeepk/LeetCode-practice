class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        map, n  = {}, len(nums)
        for i in nums:                
            map[i] = 0
        ans = 0
        for i in map:
            if i-1 not in map:
                x=i
                cnt = 1
                while x+1 in map:
                    x+=1
                    cnt+=1
                ans = max(ans,cnt)
        return ans
