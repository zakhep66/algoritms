class Solution:
    def merge(self, nums1: [int], m: int, nums2: [int], n: int):
        i = j = 0
        while i < n and j < m:
            if nums1[i] < nums2[j]:
                c.append(nums1[i])
                i += 1
            else:
                c.append(nums2[j])
                j += 1
            while i < n:
                c.append(nums1[i])
                i += 1
            while j < m:
                nums1.append(nums2[j])
                j += 1
        nums1 = c
        print(nums1)


Solution().merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3)
