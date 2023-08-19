class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {char: 0 for char in set(s + t)}
        # Count the occurrences of each character in the first string
        for x in s:
            d[x] += 1       
        # Subtract the occurrences of each character in the second string
        for x in t:
            d[x] -= 1   
        # Check if all character counts are zero, meaning both strings are anagrams
        for count in d.values():
            if count != 0:
                return False  
        return True