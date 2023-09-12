class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        cfactors = 0
        least = min(a,b)
        for i in range(1,least+1):
            if a%i == 0 and b%i == 0:
                cfactors += 1
        return cfactors        