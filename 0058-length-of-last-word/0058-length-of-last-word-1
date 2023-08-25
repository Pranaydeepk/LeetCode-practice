class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        size = len(s) - 1
        while size >= 0:
            if s[size] == ' ':
                if length > 0:
                    return length
            else:
                length += 1
            size -= 1
        return length