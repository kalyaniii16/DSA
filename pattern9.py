class Solution:
    def pattern9(self, n):

        #upper pyramid
        for i in range(n):

            for j in range(n-i-1):
                print(" ", end=" ")

            for j in range(2*i+1):
                print('*', end=" ")
            
            print()

        #lower pyramid
        for i in range(n):

            for j in range(i):
                print(" ", end=" ")

            for j in range(2*(n-i)-1):
                print('*', end=" ")

            print()

obj = Solution()
n = int(input())            
obj.pattern9(n)