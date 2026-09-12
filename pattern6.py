class Solution:
    def pattern6(self, n):
        for i in range(n):
            for j in range(n-i):
                print(j+1, end=" ")
            print()
obj = Solution()
n = int(input())            
obj.pattern6(n)