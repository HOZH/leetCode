#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start
from functools import lru_cache


class Solution:
    def numDecodings(self, s: str) -> int:
        @lru_cache(None)
        def helper(string):
            count = 0
            valid = False
            if len(string) == 0:
                return 1
            if string[0] != '0':
                temp = helper(string[1:])
                if temp != -1:
                    count += temp
                    valid = True

                if len(string) > 1:
                    if int(string[:2]) <= 26:
                        temp = helper(string[2:])
                        if temp != -1:
                            count += temp
                            valid = True
                return count if valid else -1
            else:
                return -1

        return max(helper(s), 0)


# @lc code=end
