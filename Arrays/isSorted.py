class Solution:
    def isSorted(self, nums):
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                return False
        return True

obj = Solution()
nums = [1, 1, 3, 2, 4, 5]                
print(obj.isSorted(nums))