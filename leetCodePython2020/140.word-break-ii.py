#
# @lc app=leetcode id=140 lang=python3
#
# [140] Word Break II
#

# @lc code=start

from functools import lru_cache


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        wordDict = set(wordDict)

        @lru_cache(None)
        def helper(sub1):

            temp_result = []

            if sub1 in wordDict:
                temp_result.append(sub1)

            for i in range(1, len(sub1)):

                left, right = sub1[:i], sub1[i:]

                if right in wordDict:

                    left_result = helper(left)

                    if left_result:

                        for j in left_result:
                            temp_result.append(j+' '+right)

            return temp_result if temp_result else None

        return helper(s)


# @lc code=end
