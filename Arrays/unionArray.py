class Solution:
    def unionArray(self, nums1, nums2):
        i = 0
        j = 0
        union = []

        # Compare elements while both arrays have elements
        while i < len(nums1) and j < len(nums2):

            if nums1[i] < nums2[j]:

                if not union or union[-1] != nums1[i]:
                    union.append(nums1[i])
                i += 1

            # nums2[j] is smaller OR both are equal
            else:

                if not union or union[-1] != nums2[j]:
                    union.append(nums2[j])
                j += 1

        # Remaining elements of nums1
        while i < len(nums1):
            if not union or union[-1] != nums1[i]:
                union.append(nums1[i])
            i += 1

        # Remaining elements of nums2
        while j < len(nums2):
            if not union or union[-1] != nums2[j]:
                union.append(nums2[j])
            j += 1

        return union
obj = Solution()
nums1 = [1, 2, 4, 5, 6]
nums2 = [2, 3, 5, 7]
print(obj.unionArray(nums1, nums2))