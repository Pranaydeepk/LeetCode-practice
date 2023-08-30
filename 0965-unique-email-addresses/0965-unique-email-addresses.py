class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()
        for e in emails:
            a, b = e.split('@')
            a = a.split('+')[0]
            a = a.replace('.','') + '@'
            unique.add((a, b))
        return len(unique)