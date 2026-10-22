class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        left = 0
        right = len(nums1)
        half_lenght = (len(nums1) + len(nums2) + 1) // 2
        while left <= right:
            i = left + (right - left) // 2
            j = half_lenght - i
            nums1_left = nums1[i - 1] if i > 0 else float("-inf")
            nums1_right = nums1[i] if i < len(nums1) else float("inf")

            nums2_left = nums2[j - 1] if j > 0 else float("-inf")
            nums2_right = nums2[j] if j < len(nums2) else float("inf")

            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                if (len(nums1) + len(nums2)) % 2 == 0:
                    return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2
                else:
                    return max(nums1_left, nums2_left)
            
            elif nums1_right > nums2_left:
                right = i - 1
            else:
                left = i + 1


