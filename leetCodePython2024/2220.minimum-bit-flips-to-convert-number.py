#
# @lc app=leetcode id=2220 lang=python3
#
# [2220] Minimum Bit Flips to Convert Number
#

# @lc code=start
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        start_binary_str = "{0:b}".format(start)
        goal_binary_str = "{0:b}".format(goal)
        length_of_longer_representation = max(
            len(start_binary_str), len(goal_binary_str))
        start_list, goal_list = [*start_binary_str], [*goal_binary_str]
        start_list = (['0']*(length_of_longer_representation -
                      len(start_list)))+start_list
        goal_list = (['0']*(length_of_longer_representation -
                     len(goal_list)))+goal_list

        ans = 0
        for i in range(length_of_longer_representation):
            if start_list[i] != goal_list[i]:
                ans += 1

        return ans


# @lc code=end
