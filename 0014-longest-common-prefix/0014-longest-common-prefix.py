class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        index = 0
        while index < (len(strs[0])):
            for i in strs[1:]:
                if index >= len(i) or i[index] != strs[0][index]:
                    return strs[0][0:index]
            index += 1
        return strs[0][0:index]