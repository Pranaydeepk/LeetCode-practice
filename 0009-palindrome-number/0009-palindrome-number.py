class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return True
        if x < 0 or x%10 == 0:
            return False
        else:
            rx = 0
            while x > rx:
                rx = rx*10 + x%10
                x = x//10                       
            if x == rx or x == rx//10:
                return True