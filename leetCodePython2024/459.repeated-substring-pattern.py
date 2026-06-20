#
# @lc app=leetcode id=459 lang=python3
#
# [459] Repeated Substring Pattern
#

# @lc code=start
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        candidate = ''
        for i in range(len(s)//2+1):
            candidate += s[i]
            q, r = divmod(len(s), len(candidate))
            if r == 0 and q > 1:
                if candidate * q == s:
                    return True
        return False
# "a" -> false
# "ab" -> false

# 0 0 4
# 1 0 2
# 2 1 1

# redacted = {
# "<td>"
# "<tr>"
# }
# skipped = {}

# @lc code=end
