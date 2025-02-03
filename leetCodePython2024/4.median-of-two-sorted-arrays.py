#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:

    def findMedianSortedArrays(self, A, B) -> float:

        n1, n2 = len(A), len(B)
        if n1 > n2:
            return self.findMedianSortedArrays(B, A)
        # k = m1 + m2
        k = (n1 + n2 + 1) // 2

        # boundary for m1
        l, r = 0, n1

        def min_count_from_A_contains_equal_or_greater_than_total_count(count_eles_smaller_than_median_from_A):
            count_eles_smaller_than_median_from_B = k - \
                count_eles_smaller_than_median_from_A
            # p2 is how many element need from B
            # p2 since it's 0 indexed
            return A[count_eles_smaller_than_median_from_A] >= B[count_eles_smaller_than_median_from_B-1]
            
        while l < r:
            m1 = l + (r - l) // 2
            if min_count_from_A_contains_equal_or_greater_than_total_count(m1):
                r = m1
            else:
                l = m1+1

        m1 = l
        m2 = k - l
        # m1 -1 = m1 else from A
        # m2 -1 = m2 eles from B
        # since m1,m2 is the count of eles but arrs are 0 indexed
        # print(m1)
        # print(m2)
        
        c1 = max(float('-inf') if m1 <1
                  else A[m1 - 1], float('-inf') if m2 <1 else B[m2 - 1])

        if (n1 + n2) % 2 == 1:
            # case odd numbers
            return c1

        # find next smallest ele from first median candidate
        c2 = min(float('inf') if m1 >= n1 else A[m1], float(
            'inf') if m2 >= n2 else B[m2])

        return (c1 + c2) / 2
    
t = Solution()
# print(t.findMedianSortedArrays([4, 5], [1, 2, 6, 7, 8]))
# print(t.findMedianSortedArrays([3, 4, 5], [1, 2, 6, 7, 8]))


# @lc code=end

