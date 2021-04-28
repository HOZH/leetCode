#
# @lc app=leetcode id=763 lang=python3
#
# [763] Partition Labels
#

# @lc code=start
class Solution:
    def partitionLabels(self, S: str):
        last = {c: i for i, c in enumerate(S)}
        j, start = 0, 0
        ans = []

        for i, c in enumerate(S):
            j = max(j, last[c])
            if i == j:
                ans.append(i - start + 1)
                start = i + 1

        return ans

# @lc code=end
