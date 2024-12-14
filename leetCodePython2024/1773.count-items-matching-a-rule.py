#
# @lc app=leetcode id=1773 lang=python3
#
# [1773] Count Items Matching a Rule
#

# @lc code=start

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        ans = 0
        for type, color, name in items:

            match ruleKey:
                case 'type':
                    if ruleValue == type:
                        ans += 1
                case 'color':
                    if ruleValue == color:
                        ans += 1
                case 'name':
                    if ruleValue == name:
                        ans += 1
                case _:
                    pass

        return ans

# @lc code=end
