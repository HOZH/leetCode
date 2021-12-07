#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # temp1, temp2 = nums1[:m], nums2[:n]
        # ans = []

        # while len(temp1) or len(temp2):
        #     if not len(temp1):
        #         ans.extend(temp2)
        #         break
        #     if not len(temp2):
        #         ans.extend(temp1)
        #         break
        #     head_1, head_2 = temp1[0], temp2[0]

        #     if head_1 <= head_2:
        #         ans.append(head_1)
        #         temp1 = temp1[1:]
        #     else:
        #         ans.append(head_2)
        #         temp2 = temp2[1:]

        # for i in range(len(ans)):
        #     nums1[i] = ans[i]

        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1

        nums1[:n] = nums2[:n]


# @lc code=end
