#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#

# @lc code=start


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:

        length, a, b, result = len(A), -1, -1, []

        if length == 1:
            return [A[0]**2]

        for i in range(length):
            if A[i] >= 0:
                a = i-1
                b = i
                break
            else:
                a = i
                b = -1

        if b == -1:
            return list(map(lambda x: x**2, A[::-1]))
        elif a == -1:
            return list(map(lambda x: x**2, A))

        while a >= 0 and b < length:
            p1, p2 = A[a]**2, A[b]**2

            if p1 >= p2:
                result.append(p2)
                b += 1
            else:
                result.append(p1)
                a -= 1

        # when one of the pointer reach the end, we mannually add the remaining eles to the end
        for i in range(a, -1, -1) if a > -1 else range(b, length):
            result.append(A[i]**2)

        return result
        # @lc code=end
