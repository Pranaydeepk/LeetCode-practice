class Solution:
    def isValid(self, s: str) -> bool:
        d = {'(':')','{':'}','[':']'}
        stack = []
        for i in s:
            if i in d:
                stack.append(i)
            else:
                if not stack:
                    return False
                if i != d[stack[-1]]:
                    return False
                else:
                    stack.pop()
        if stack:
            return False
        else:
            return True