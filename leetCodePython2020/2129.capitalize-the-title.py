#
# @lc app=leetcode id=2129 lang=python3
#
# [2129] Capitalize the Title
#

# @lc code=start
class Solution:
    def capitalizeTitle(self, title: str) -> str:
        title = [*title.lower()]
        placeholder = title[:]
        for i in range(len(title)):
            if title[i] == ' ':
                placeholder[i+1] = placeholder[i+1].upper()
        placeholder[0] = placeholder[0].upper()
        placeholder = ''.join(placeholder)
        placeholder = placeholder.split(' ')
        ans = ''
        for i in placeholder:
            if len(i) < 3:
                ans += ''.join(i).lower()
            else:
                ans += ''.join(i)
            ans += ' '
        return ans[:-1]

# @lc code=end
