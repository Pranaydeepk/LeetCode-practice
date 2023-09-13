class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        prefix_len = len(pref)
        for word in words:
            word_len = len(word)
            if word_len < prefix_len:
                continue
            is_prefix = True
            for i in range(prefix_len):
                if word[i] != pref[i]:
                    is_prefix = False
                    break
            if is_prefix:
                count += 1
        return count