#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
from functools import lru_cache


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)

        @lru_cache(None)
        def helper(sub):
            if sub in wordSet:
                return True

            for i in range(1, len(sub)):
                left, right = sub[:i], sub[i:]
                if left in wordSet and helper(right):
                    return True

            return False

        return helper(s)

# @lc code=end
