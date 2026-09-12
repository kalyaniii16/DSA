# Given a digit d (0 to 9), find the sum of first 50
#positive integers (integer >0) that end with digit d.
class Solution:
    def whileLoop(self, d):
        total = 0
        n = 50

        if d == 0:
            d = 10

        while n > 0:
            total = total + d
            d = d + 10
            n -= 1
        print(total)

obj = Solution()
d = int(input())
obj.whileLoop(d)