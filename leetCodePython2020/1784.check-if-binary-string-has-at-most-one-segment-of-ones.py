#
# @lc app=leetcode id=1784 lang=python3
#
# [1784] Check if Binary String Has at Most One Segment of Ones
#

# @lc code=start
class Solution:
    def checkOnesSegment(self, s: str) -> bool:

        start = s.find('1')
        flag = True

        for i in range(start+1, len(s)):
            if s[i] == '1':
                if not flag:
                    return False

            elif s[i] == '0':
                flag = False

        return True

# @lc code=end
