#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start


class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:

        mem = dict()
        wd = set(wordDict)
        mem[''] = True

        def helper(sub1, m, d):

            if sub1 in m:
                return m[sub1]

            elif sub1 in d:
                m[sub1] = True
                return True

            for i in range(1, len(sub1)):

                left, right = sub1[:i], sub1[i:]
                if right in d and helper(left, m, d):
                    m[sub1] = True
                    return True
            m[sub1] = False
            return False

        return helper(s, mem, wd)

# @lc code=end
