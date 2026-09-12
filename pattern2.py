class Solution:
    def pattern2(self, n):
        for i in range(n):
            for j in range(i+1):
                print("*", end=" ")
            print()
obj = Solution()
n = int(input())
obj.pattern2(n)            