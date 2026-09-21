class Solution:
    def maxSubArray(self, nums):
        sum = 0
        maxi = float('-inf')

        for i in range(len(nums)):
            sum += nums[i]

            maxi = max(maxi, sum)

            if sum < 0:
                sum = 0

        return maxi
obj = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,7]
print(obj.maxSubArray(nums))