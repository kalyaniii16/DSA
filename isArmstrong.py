class Solution:
    def isArmstrong(self, n):
        num = n
        sum = 0
        digits = len(str(n))

        while n > 0:
            last_digit = n % 10
            sum = sum + last_digit ** digits
            n = n // 10
            
        return sum == num

obj = Solution()
n = int(input())
print(obj.isArmstrong(n))