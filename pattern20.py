class Solution:
    def pattern20(self, n):

        #upper half
        for i in range(n):
            for j in range(i+1):
                print('*', end=" ")
            for j in range(2*(n-i-1)):
                print(" ", end=" ")
            for j in range(i+1):
                print('*', end=" ")
            print()

        #lower half
        for i in range(n-1):
            for j in range(n-i-1):
                print('*', end=" ")
            for j in range(2*(i+1)):
                print(" ", end=" ")
            for j in range(n-i-1):
                print('*', end=" ")
            print()
obj = Solution()
n=int(input())
obj.pattern20(n)
