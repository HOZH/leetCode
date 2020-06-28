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

        while l < r:
            m1 = l + (r - l) // 2
            m2 = k - m1
            # m2-1 since it's 0 indexed
            if A[m1] < B[m2 - 1]:
                # need more ele from A, raising m1
                l = m1 + 1

            else:
                r = m1

        m1 = l
        m2 = k - l
        c1 = max(float('-inf') if m1 <=
                 0 else A[m1 - 1], float('-inf') if m2 <= 0 else B[m2 - 1])

        if (n1 + n2) % 2 == 1:
            # case odd numbers
            return c1

        c2 = min(float('inf') if m1 >= n1 else A[m1], float(
            'inf') if m2 >= n2 else B[m2])

        return (c1 + c2) / 2


# @lc code=end
