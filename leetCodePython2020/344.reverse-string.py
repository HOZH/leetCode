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
        length = len(s)
        if not length:
            return []

        current_index = 0
        temp = None

        while current_index < length//2:
            tail_index = -(current_index+1)
            temp = s[tail_index]

            s[tail_index] = s[current_index]
            s[current_index] = temp

            current_index += 1

        return s


# @lc code=end
