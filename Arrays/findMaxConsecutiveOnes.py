class Solution:
    def findMaxConsecutiveOnes(self, nums):
        cnt = 0
        maxi = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                cnt += 1
                maxi = max(maxi, cnt)
            else:
                cnt = 0
        return maxi
obj = Solution()
nums = [1, 1, 0, 1, 1, 1, 0, 1, 1]
print(obj.findMaxConsecutiveOnes(nums))