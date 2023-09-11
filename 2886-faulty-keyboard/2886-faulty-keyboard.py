class Solution:
    def finalString(self, s: str) -> str:
        result, temp = '', ''
        for i in s:
            if i != 'i':
                result += i
            else:
                temp = result[::-1]
                result = temp
        return result        