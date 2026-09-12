class Solution:
    def pattern11(self, n):

        #number of rows
        for i in range(n):

            #no. of elements in each row
            for j in range(i+1):

                if (i+j) % 2 == 0:
                    print(1, end=" ")
                else:
                    print(0, end=" ")

            print()
obj=Solution()
n=int(input())
obj.pattern11(n)            