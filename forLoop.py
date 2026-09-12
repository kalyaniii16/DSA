class Solution:
    def forLoop(self, low, high):
        total = 0
        for i in range (low, high+1):
            total += i
        return total
obj = Solution()
low = int(input())
high = int(input())
print(obj.forLoop(low, high))