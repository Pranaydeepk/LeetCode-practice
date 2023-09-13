class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        n = len(arr)
        for i in range(1,n-1):
            if arr[i-1]%2 ==1 and arr[i]%2 ==1 and arr[i+1]%2 ==1:
                return True
        return False