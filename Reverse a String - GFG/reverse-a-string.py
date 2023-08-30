#User function Template for python3

class Solution:
    def reverseWord(self, s):
        #your code here
        i, j, reverse = 0, len(s) - 1, ''
        s = list(s)
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        for i in s:
            reverse += i
        return reverse


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while(t>0):
        s = input()
        ob = Solution()
        print(ob.reverseWord(s))
        t = t-1

# } Driver Code Ends