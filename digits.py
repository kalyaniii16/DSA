class Solution:
    def countDigits(self, n):
        return len(str(n))
    
obj = Solution()
n = int(input())
print(obj.countDigits(n))