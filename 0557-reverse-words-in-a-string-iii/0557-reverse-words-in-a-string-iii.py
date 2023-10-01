class Solution:
    def reverseWords(self, s: str) -> str:
        word = ''
        result = ''
        for i in range(len(s)):
            if s[i] != ' ' and i != len(s)-1:
                word += s[i]
            elif s[i] != ' ' and i == len(s)-1:
                word += s[-1]
                result += word[::-1]
                word = ''
            else:
                result += word[::-1] + ' '
                word = ''
        return result