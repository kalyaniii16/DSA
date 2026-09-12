class Solution:
    def largestElement(self, nums):
        largest = nums[0]

        for i in nums:
            if i > largest:
                largest = i
        return largest

obj = Solution()
nums = [5, 7, -2, 3, 10]
print(obj.largestElement(nums))