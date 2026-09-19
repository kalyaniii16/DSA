class Solution:
    def twoSum(self, nums, target):
        mp = {}

        for i in range(len(nums)):
            num = nums[i]
            moreNeeded = target - num

            if moreNeeded in mp:
                return [mp[moreNeeded], i]

            mp[num] = i

obj = Solution()
nums = [2, 7, 11, 15]
target = 9
print(obj.twoSum(nums, target))