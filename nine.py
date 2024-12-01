class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        len1, len2 = len(nums1), len(nums2)
        
        left, right = 0, len1
        
        while left <= right:
            partition1 = (left + right) // 2
            partition2 = (len1 + len2 + 1) // 2 - partition1
            
            maxLeft1 = nums1[partition1 - 1] if partition1 > 0 else float('-inf')
            minRight1 = nums1[partition1] if partition1 < len1 else float('inf')
            
            maxLeft2 = nums2[partition2 - 1] if partition2 > 0 else float('-inf')
            minRight2 = nums2[partition2] if partition2 < len2 else float('inf')
            
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                if (len1 + len2) % 2 == 1:
                    return max(maxLeft1, maxLeft2)
                else:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0
            elif maxLeft1 > minRight2:
                right = partition1 - 1
            else:
                left = partition1 + 1
                
        raise ValueError("input arrays are not sorted or valid.")
        
if __name__ == "__main__":
    solution = Solution()
    result = solution.findMedianSortedArrays([1, 3], [2])
    print(result)
