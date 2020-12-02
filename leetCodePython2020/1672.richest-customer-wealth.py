#
# @lc app=leetcode id=1672 lang=python3
#
# [1672] Richest Customer Wealth
#

# @lc code=start
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:

        if not len(accounts):
            return 0

        return max(list(map(lambda x: sum(x),accounts)))

# @lc code=end
