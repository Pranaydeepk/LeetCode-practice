class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        st = {} # for mapping letters from s --> t
        ts = {} # for mapping letters from t --> s
        for i in range(len(s)):
            if s[i] in st:
                if st[s[i]] != t[i]:
                    return False
            else:
                st[s[i]] = t[i] 
            if t[i] in ts:
                if ts[t[i]] != s[i]:
                    return False
            else:
                ts[t[i]] = s[i]
        return True