class Solution:
    def digitCount(self, num: str) -> bool:
        size = len(num)
        freq = {}
        for i in range(size):
            freq[str(i)] = 0
        for i in range(size):
            if num[i] in freq:
                freq[num[i]] += 1
        for i in range(size):
            if num[i] != str(freq[str(i)]):
                return False
        return True