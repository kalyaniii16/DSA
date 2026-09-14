class Solution:
    def leftRotateArray(self, nums, k):
        k = k % len(nums)

        # reverse first k elements
        first = 0
        last = k - 1
        while first < last:
            nums[first], nums[last] = nums[last], nums[first]
            first += 1
            last -= 1

        # reverse remaining elements
        first = k
        last = len(nums) - 1
        while first < last:
            nums[first], nums[last] = nums[last], nums[first]
            first += 1
            last -= 1

        # reverse entire array
        first = 0
        last = len(nums) - 1
        while first < last:
            nums[first], nums[last] = nums[last], nums[first]
            first += 1
            last -= 1
        return nums
obj = Solution()
nums = [7, 8, 9, 10, 11, 12, 13]
k = 3
print(obj.leftRotateArray(nums, k))