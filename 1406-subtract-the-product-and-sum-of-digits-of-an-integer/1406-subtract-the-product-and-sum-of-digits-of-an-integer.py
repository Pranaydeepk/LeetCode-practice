class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        total = 0
        while n > 0:
            product *= n%10
            total += n%10
            n = n//10
        return product - total