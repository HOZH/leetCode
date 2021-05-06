#
# @lc app=leetcode id=861 lang=python3
#
# [861] Score After Flipping Matrix
#

# @lc code=start
class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])
        # a list to count 1 in each column
        col = [0] * n
        for i in range(m):
            # start from the right, so we can use A[i][0] as a reference
            for j in range(n-1, -1, -1):
                # flip row if start of this row is 0
                A[i][j] = (1-A[i][j]) if not A[i][0] else A[i][j]
                col[j] += A[i][j]
        # flip column when necessary
        for j in range(1, n):
            if (m % 2 and col[j] <= m // 2) or (not m % 2 and col[j] < m // 2):
                for i in range(m):
                    A[i][j] = 1-A[i][j]
        # calculate the sum
        return sum(sum(2**(n-1-j) * A[i][j] for j in range(n)) for i in range(m))

# @lc code=end
