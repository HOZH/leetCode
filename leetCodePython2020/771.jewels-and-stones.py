#
# @lc app=leetcode id=771 lang=python3
#
# [771] Jewels and Stones
#

# @lc code=start


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:

        jewels = set(J)
        count = 0

        return len(list(filter(lambda x: x in jewels, list(S))))

# @lc code=end
