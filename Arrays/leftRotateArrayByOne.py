class Solution:
    def leftRotateArrayByOne(self, nums):
        first = nums[0]

        for i in range(len(nums)-1):
            nums[i] = nums[i+1]

        nums[len(nums)-1] = first
        return nums

obj = Solution()
nums = [1, 2, 3, 4, 5]
print(obj.leftRotateArrayByOne(nums)) 