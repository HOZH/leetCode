#
# @lc app=leetcode id=2315 lang=python3
#
# [2315] Count Asterisks
#

# @lc code=start
class Solution:
    def countAsterisks(self, s: str) -> int:

        marks = []
        for i in range(len(s)):
            if s[i] == '|':
                marks.append(i)
        ignore_count = 0
        for i in range(0, len(marks), 2):
            head = marks[i]
            tail = marks[i+1]
            ignore_count += s[head:tail+1].count('*')
        return s.count('*')-ignore_count


# @lc code=end
