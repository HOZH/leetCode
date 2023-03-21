#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l = 0
        output = 0
        for r in range(len(s)):
            """
            If s[r] not in seen, we can keep increasing the window size by moving right pointer
            """
            if s[r] not in seen:
                output = max(output, r-l+1)
            # There are two cases if s[r] in seen:
            else:
                # case1: s[r] is not inside the current window, we can keep increase the window
                if seen[s[r]] < l:
                    output = max(output, r-l+1)
                # case2: s[r] is inside the current window, we need to change the window by moving left pointer to seen[s[r]] + 1.

                else:
                    l = seen[s[r]] + 1
            seen[s[r]] = r
        return output

    # def lengthOfLongestSubstring(self, s: str) -> int:

    #     ans = 0
    #     for i in range(len(s)):
    #         current_set = set()
    #         for j in range(i, len(s)):
    #             current = s[j]
    #             if current in current_set:
    #                 break
    #             else:
    #                 current_set.add(current)
    #         ans = max(ans, len(current_set))
    #     return ans

# @lc code=end
