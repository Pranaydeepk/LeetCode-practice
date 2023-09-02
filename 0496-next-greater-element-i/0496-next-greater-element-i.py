class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [-1 for _ in range(len(nums1))]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    for p in range(j, len(nums2)):
                        if nums2[p] > nums1[i]:
                            ans[i] = nums2[p]
                            break
        return ans