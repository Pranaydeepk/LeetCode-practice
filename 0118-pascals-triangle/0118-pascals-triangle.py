class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        level = 1
        while numRows >= level:
            row = [[0 for _ in range(level)]]
            result += row
            level += 1
        level = 0
        while level < numRows:
            if level == 0:
                result[level][0] = 1
            if level == 1:
                for i in range(level+1):
                    result[level][i] = 1
            else:
                for i in range(level+1):
                    if i == 0 or i == level:
                        result[level][i] = 1
                    else:
                        result[level][i] = result[level-1][i-1] + result[level-1][i]
            level += 1
        return result
