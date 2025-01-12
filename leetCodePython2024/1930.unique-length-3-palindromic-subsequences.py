#
# @lc app=leetcode id=1930 lang=python3
#
# [1930] Unique Length-3 Palindromic Subsequences
#

# @lc code=start
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ans = 0
        found = set()
        for i in range(len(s)):
            current = s[i]
            if current not in found:
                found.add(current)
            else:
                continue
            last_index_of_current_char = s.rfind(current)
            if last_index_of_current_char != i:
                ans += len(set(s[i+1:last_index_of_current_char]))
        # for i in range(len(s)):
        #     for j in range(i+1, len(s)):
        #         for k in range(j+1, len(s)):
        #             if s[k] == s[i]:
        #                 temp = s[i]+s[j]+s[k]
        #                 if temp not in found:
        #                     found.add(temp)
        #                     ans += 1

        return ans


# @lc code=end
