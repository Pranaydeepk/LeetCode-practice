class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()
        for e in emails:
            i, a = 0, ''
            while i < len(e) and e[i] != '@' and e[i] != '+':
                if e[i] == '.':
                    i += 1
                    continue
                a += e[i]
                i += 1
            while i < len(e) and e[i] != '@':
                i += 1
            while i < len(e):
                a += e[i]
                i += 1
            unique.add(a)
        return len(unique)