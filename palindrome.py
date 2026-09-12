class Solution:
    def isPalindrome(self, n):
        original = n
        rev = 0

        while n > 0:
            last_digit = n % 10
            rev = rev*10 + last_digit
            n = n // 10

        return original == rev

obj = Solution()
n = int(input())
print(obj.isPalindrome(n))