#
# @lc app=leetcode id=1163 lang=python3
#
# [1163] Last Substring in Lexicographical Order
#

# @lc code=start


class Solution:

    def lastSubstring(self, s: str) -> str:

        start_char = max(s)
        ans = start_char

        # for i in range(len(s)):
        #     if s[i] > start_char:
        #         start_char = s[i]

        for i in range(len(s)):
            if s[i] == start_char:
                ans = max(ans, s[i:])

        return ans

        # @lc code=end
