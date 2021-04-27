#
# @lc app=leetcode id=1689 lang=python3
#
# [1689] Partitioning Into Minimum Number Of Deci-Binary Numbers
#

# @lc code=start
class Solution:
    def minPartitions(self, n: str) -> int:

        temp = [int(i) for i in n]

        count = 0

        for i in range(len(temp)):
            current = temp[i]
            if current == 0:
                continue
            for j in range(i, len(temp)):
                temp[j] = max(0, temp[j]-current)

            count += current

        return count


# @lc code=end
