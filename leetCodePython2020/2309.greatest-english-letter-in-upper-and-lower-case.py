#
# @lc app=leetcode id=2309 lang=python3
#
# [2309] Greatest English Letter in Upper and Lower Case
#

# @lc code=start
from collections import defaultdict


class Solution:
    def greatestLetter(self, s: str) -> str:
        uppers = defaultdict(bool)
        lowers = defaultdict(bool)
        for i in s:
            current = ord(i)
            if 97 <= current < 123:
                lowers[current] = True
            else:
                uppers[current+32] = True

        for i in range(122, 96, -1):
            if lowers[i] and uppers[i]:
                return chr(i-32)

        return ""

# @lc code=end
