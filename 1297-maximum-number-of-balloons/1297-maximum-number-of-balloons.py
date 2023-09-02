class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d = {}
        for _ in 'balon':
            d[_] = 0
        for i in range(len(text)):
            if text[i] in d:
                d[text[i]] += 1
        # b, a, n, l, o = 0, 0, 0, 0, 0
        ans = 1000000000
        for x,y in d.items():
            if x in 'lo':
               ans = min(y//2, ans)
            else:
                ans = min(y, ans)
        return ans


        