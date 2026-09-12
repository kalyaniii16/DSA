class Solution:
    def pattern19(self, n):
        
        # upper half
        for i in range(n):
            for j in range(n-i):
                print('*', end=" ")
            for j in range(2*i):
                print(" ", end=" ")
            for j in range(n-i):
                print('*', end=" ")
            print()

        # lower half
        for i in range(n):
            for j in range(i+1):
                print('*', end=" ")
            for j in range(2*(n-i-1)):
                print(" ", end=" ")
            for j in range(i+1):
                print('*', end=" ")
            print()
obj=Solution()
n=int(input())
obj.pattern19(n)            