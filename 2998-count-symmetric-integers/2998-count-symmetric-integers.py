class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for i in range(low, high + 1):
            if len(str(i)) % 2 == 0:
                digits = []
                while i > 0:
                    temp = i % 10
                    digits.append(temp)
                    i = i // 10
                s = len(digits) // 2
                if sum(digits[:s]) == sum(digits[s:]):
                    count += 1
        return count