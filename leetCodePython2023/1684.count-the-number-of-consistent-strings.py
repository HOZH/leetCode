#
# @lc app=leetcode id=1684 lang=python3
#
# [1684] Count the Number of Consistent Strings
#

# @lc code=start
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set([*allowed])
        return list(map(lambda x: all([(i in allowed)for i in [*x]]), words)).count(True)

# @lc code=end
