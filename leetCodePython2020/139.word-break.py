#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start

from functools import lru_cache


class Solution:
    def wordBreak(self, s: str, wordDict):

        # mem = dict()
        wordDict = set(wordDict)
        # mem[''] = True

        # def helper(sub1):

        #     if sub1 in mem:
        #         return mem[sub1]

        #     elif sub1 in wordDict:
        #         mem[sub1] = True
        #         return True

        #     for i in range(1, len(sub1)):
        #         left, right = sub1[:i], sub1[i:]
        #         if right in wordDict and helper(left):
        #             mem[sub1] = True
        #             return True

        #     mem[sub1] = False
        #     return False

        # return helper(s)

        @lru_cache(None)
        def helper_with_lrc(sub1):
            if sub1 in wordDict:
                return True
            for i in range(1, len(sub1)):
                left, right = sub1[:i], sub1[i:]
                if right in wordDict and helper_with_lrc(left):
                    return True

            return False

        return helper_with_lrc(s)


# @lc code=end
