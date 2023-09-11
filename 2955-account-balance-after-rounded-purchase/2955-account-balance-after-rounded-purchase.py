class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        deduction = 0
        if purchaseAmount <= 10:
            if purchaseAmount < 5:
                deduction = 0
            else:
                deduction = 10
        else:
            if purchaseAmount < (purchaseAmount//10)*10+5:
                deduction = (purchaseAmount//10)*10
            else:
                deduction = (purchaseAmount//10)*10+10
        return 100 - deduction