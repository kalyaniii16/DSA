class Solution:
    def pattern7(self, n):
        # print rows
        for i in range(n):

            #print spaces
            for j in range(n-i-1):
                print(" ", end=" ")

            #print stars
            for j in range(2*i + 1):
                print('*', end=" ")

            print()
obj = Solution()
n = int(input())            
obj.pattern7(n)
            