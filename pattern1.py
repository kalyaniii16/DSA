class Solution:
    def pattern1(self, n):
        #number of rows
        for i in range(n):
            #number of elements to be printed in each row
            for j in range(n):
                print("*", end=" ")
            #move to next line after finishing one row
            print()
obj = Solution()                
n = int(input())
obj.pattern1(n)