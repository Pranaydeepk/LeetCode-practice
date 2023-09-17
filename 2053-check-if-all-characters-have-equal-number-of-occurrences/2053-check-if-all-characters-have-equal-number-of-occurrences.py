class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        freq = d[s[0]]
        for x,y in d.items():
            if y != freq:
                return False
        return True