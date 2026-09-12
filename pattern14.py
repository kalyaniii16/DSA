class Solution:
    def pattern14(self, n):
        for i in range(n):
            for j in range(i+1):
                print(chr(65 + j), end=" ")
            print()
obj = Solution()            
n=int(input())
obj.pattern14(n)