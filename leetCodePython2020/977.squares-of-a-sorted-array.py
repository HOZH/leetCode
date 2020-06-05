#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#

# @lc code=start


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:

        length = len(A)
        if length == 1:
            return [A[0]**2]

        a, b = -1, -1
        for i in range(length):
            if A[i] >= 0:
                a = i-1
                b = i
                break
        result = []

        while a >= 0 and b < length:
            p1, p2 = A[a]**2, A[b]**2

            if p1 >= p2:
                result.append(p2)
                b += 1
            else:
                result.append(p1)
                a -= 1
        for i in range(a, -1, -1) if a > -1 else range(b, length):
            result.append(A[i]**2)

        return result
        # @lc code=end
