class Solution:
    def reverseNumber(self, n):
        rev=0

        while n>0:
            lastdigit = n % 10 #Remainder
            rev = rev*10 + lastdigit
            n = n // 10 #quotient
        return rev
obj = Solution()
n = int(input())
print(obj.reverseNumber(n))