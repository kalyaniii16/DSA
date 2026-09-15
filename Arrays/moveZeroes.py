class Solution:
    def moveZeroes(self, nums):
        j = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                j = i
                break

        if j == -1:
            return nums

        for i in range(j + 1, len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        return nums
obj = Solution()
nums = [1,2,0,0,5,7,4,0]
print(obj.moveZeroes(nums))