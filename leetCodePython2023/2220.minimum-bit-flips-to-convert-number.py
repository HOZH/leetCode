#
# @lc app=leetcode id=2220 lang=python3
#
# [2220] Minimum Bit Flips to Convert Number
#

# @lc code=start
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        start_bin = bin(start).removeprefix('0b')
        goal_bin = bin(goal).removeprefix('0b')

        ans = 0
        max_len = max(len(start_bin), len(goal_bin))
        fill = max_len-len(start_bin)
        start_bin = '0'*fill+start_bin
        fill = max_len-len(goal_bin)
        goal_bin = '0'*fill+goal_bin

        for i in range(len(goal_bin)):
            if start_bin[i] != goal_bin[i]:
                ans += 1

        return ans

# @lc code=end
