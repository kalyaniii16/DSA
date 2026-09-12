class Solution:
    def pattern22(self, n):
        size = 2*n - 1

        for i in range(size):
            for j in range(size):
                top = i
                left = j
                bottom = size-1-i
                right = size-1-j

                value = n - min(top, left, bottom, right)
                print(value, end=" ")

            print()
obj=Solution()
n=int(input())            
obj.pattern22(n)