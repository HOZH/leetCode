#
# @lc app=leetcode id=1823 lang=python3
#
# [1823] Find the Winner of the Circular Game
#

# @lc code=start
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:

        if n == 0:
            return None
        if n == 1:
            return 1
        group = [i for i in range(1, n+1)]

        current_index = 0

        while len(group) > 1:

            current_index += k-1
            current_index = current_index % n

            group.pop(current_index)

            n -= 1

        return group[0]


# @lc code=end
