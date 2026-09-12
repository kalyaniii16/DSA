class Solution:
    def pattern12(self, n):

        #number of rows
        for i in range(1, n+1):
            
            #print increasing numbers
            for j in range(1, i+1):
                print(j, end="")

            #print spaces
            for j in range(2*(n-i)):
                print(" ", end="")

            #print reverse numbers
            for j in range(i, 0, -1):
                print(j, end="")

            print()

obj = Solution()
n = int(input())
obj.pattern12(n)             