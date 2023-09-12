class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth,n = [], len(accounts)
        for i in range(n):
            wealth.append(sum(accounts[i]))
        return max(wealth)