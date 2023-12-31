class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        prefix_len = len(pref)
        for word in words:
            if len(word) >= prefix_len:
                is_prefix = True
                for i in range(prefix_len):
                    if word[i] != pref[i]:
                        is_prefix = False
                        break
                if is_prefix:
                    count += 1
        return count