class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        n = len(height)
        lmax, rmax, traps = [0]*n, [0]*n, [0]*n
        lmax[0] = height[0]
        rmax[n-1] = height[n-1]
        for i in range(1,n-1):
            lmax[i] = max(lmax[i-1],height[i])
        for i in range(n-2,0,-1):
            rmax[i] = max(rmax[i+1],height[i])
        for i in range(1,n-1):
            traps[i] = min(lmax[i],rmax[i]) - height[i]
        return sum(traps)
        