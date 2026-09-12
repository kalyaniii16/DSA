class Solution:
    def pattern18(self, n):
        for i in range(n):

            ch = 65 + (n-i-1)
            for j in range(i+1):
                print(chr(ch), end=" ")
                ch += 1
            
            print()
obj = Solution()
n = int(input())            
obj.pattern18(n)
