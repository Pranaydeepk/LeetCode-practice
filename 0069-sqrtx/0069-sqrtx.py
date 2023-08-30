class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        root = 1
        while (root+1)*(root+1) < x:
            root += 1
        if (root+1)*(root+1) == x:
                return root+1
        return root