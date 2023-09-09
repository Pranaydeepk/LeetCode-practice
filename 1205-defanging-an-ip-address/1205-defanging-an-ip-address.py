class Solution:
    def defangIPaddr(self, address: str) -> str:
        defanged = ''
        for i in range(len(address)):
            if address[i] != '.':
                defanged += address[i]
            else:
                defanged += '[.]'
        return defanged
        