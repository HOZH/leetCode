#
# @lc app=leetcode id=2351 lang=python3
#
# [2351] First Letter to Appear Twice
#

# @lc code=start
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        bag = set()
        for i in s:
            if i in bag:
                return i
            bag.add(i)


# @lc code=end
