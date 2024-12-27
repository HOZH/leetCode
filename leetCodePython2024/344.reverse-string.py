#
# @lc app=leetcode id=344 lang=python3
#
# [344] Reverse String
#

# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        head, tail = 0, len(s)-1
        while head < tail:
            prev_tail_val = s[tail]
            s[tail] = s[head]
            s[head] = prev_tail_val
            head += 1
            tail -= 1


# @lc code=end
