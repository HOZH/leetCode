#
# @lc app=leetcode id=2027 lang=python3
#
# [2027] Minimum Moves to Convert String
#

# @lc code=start
class Solution:
    def minimumMoves(self, s: str) -> int:

        count = 0
        covered_len = 0
        for i in range(len(s)):
            current = s[i]
            if current == 'O':
                covered_len = max(0, covered_len-1)
            elif current == 'X':
                if covered_len != 0:
                    covered_len -= 1
                else:
                    count += 1
                    covered_len = 2

        return count


# @lc code=end
