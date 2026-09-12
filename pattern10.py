class Solution:
    def pattern10(self, n):
        for i in range(n):
            for j in range(i+1):
                print('*', end=" ")

            print()
            
        for i in range(1, n):
            for j in range(n-i):
                print('*', end=" ")

            print()

obj=Solution()
n=int(input())
obj.pattern10(n)        