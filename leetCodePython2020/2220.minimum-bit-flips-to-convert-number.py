#
# @lc app=leetcode id=2220 lang=python3
#
# [2220] Minimum Bit Flips to Convert Number
#

# @lc code=start
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # start_bit_str = '{0:032b}'.format(start)
        # goal_bit_str = '{0:032b}'.format(goal)

        # result = 0
        # for i in range(len(start_bit_str)):
        #     if start_bit_str[i] != goal_bit_str[i]:
        #         result += 1
        # return result

        return (start ^ goal).bit_count()


# @lc code=end
