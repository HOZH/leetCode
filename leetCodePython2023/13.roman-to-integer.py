#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start

class Solution:
    def romanToInt(self, s: str) -> int:
        prev = ''
        ans = 0
        for i in s:
            if i == 'I':
                ans += 1
            elif i == 'V' or i == 'X':
                if prev == 'I':
                    ans += (4-1) if i == 'V' else (9-1)
                else:
                    ans += 5 if i == 'V' else 10
            elif i == 'L' or i == 'C':
                if prev == 'X':
                    ans += (40-10) if i == 'L' else (90-10)
                else:
                    ans += 50 if i == 'L' else 100
            elif i == 'D' or i == 'M':
                if prev == 'C':
                    ans += (400-100) if i == 'D' else (900-100)
                else:
                    ans += 500 if i == 'D' else 1000
            prev = i
        return ans

# @lc code=end
