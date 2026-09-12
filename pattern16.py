class Solution:
    def pattern16(self, n):
        for i in range(n):
            for j in range(i+1):
                print(chr(65+i), end=" ")
            print()
obj=Solution()
n=int(input())            
obj.pattern16(n)