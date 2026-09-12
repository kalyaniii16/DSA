class Solution:
    def secondLargestElement(self, nums):
        largest = nums[0]
        secondLargest = None

        for i in nums:
            if i > largest:
                secondLargest = largest
                largest = i

            if i < largest and (secondLargest is None or i > secondLargest):
                secondLargest = i

        if secondLargest is None:
            return -1
        else:
            return secondLargest

obj = Solution()
nums = [7, 7, 2, 2, 2, 10, 10]
print(obj.secondLargestElement(nums))

