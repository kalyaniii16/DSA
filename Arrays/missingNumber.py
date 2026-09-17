class Solution:
    def missingNumber(self, nums):
      
        xor = 0

        # XOR all numbers from 0 to n
        # Example: if n = 5 → 0, 1, 2, 3, 4, 5
        for i in range(len(nums) + 1):
            xor = xor ^ i

        # XOR all the numbers present in the array
        for num in nums:
            xor = xor ^ num

        # All numbers that appear twice cancel each other
        # The number left is the missing number
        return xor

obj = Solution()
nums = [3, 0, 1]
print(obj.missingNumber(nums))