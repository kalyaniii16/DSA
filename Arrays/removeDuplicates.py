class Solution:
    def removeDuplicates(self, nums):
        j = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j += 1
        return j

obj = Solution()
nums = [1, 2, 3, 3, 4, 4, 7]
print(obj.removeDuplicates(nums))