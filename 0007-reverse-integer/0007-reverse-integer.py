class Solution:
    def reverse(self, x: int) -> int:
        rx = 0
        isNegative = False
        if x < 0:
            isNegative = True
            x = -x
        while x > 0:
            rx = rx*10 + x%10
            x = x//10
        if not (-2**31 <= rx and rx <= 2**31 - 1):
            return 0
        if isNegative == False:
            return rx
        else:
            return -rx