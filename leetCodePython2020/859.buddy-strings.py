#
# @lc app=leetcode id=859 lang=python3
#
# [859] Buddy Strings
#

# @lc code=start
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:

        if len(s) != len(goal):
            return False
        if not len(s):
            return False
        if s == goal:
            if len(s)-len(set(s)) < 1:
                return False
            else:
                return True

        diff_count = 0
        s_set, goal_set = set(), set()
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff_count += 1
                s_set.add(s[i])
                goal_set.add(goal[i])
            if diff_count > 2:
                return False

        return s_set == goal_set


# @lc code=end
