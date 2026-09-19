class Solution:
    def majorityElement(self, nums):
        cnt = 0
        el = 0

        # First loop: find the candidate
        for i in range(len(nums)):
            if cnt == 0:
                cnt = 1
                el = nums[i]

            elif nums[i] == el:
                cnt += 1

            else:
                cnt -= 1

        # Second loop: count actual occurrences of candidate
        cnt1 = 0

        for i in range(len(nums)):
            if nums[i] == el:
                cnt1 += 1

        # Check if candidate is actually a majority
        if cnt1 > len(nums) // 2:
            return el

        return -1
obj = Solution()
nums = [2,2,1,1,1,2,2]
print(obj.majorityElement(nums))