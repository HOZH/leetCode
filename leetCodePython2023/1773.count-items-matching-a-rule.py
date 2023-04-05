#
# @lc app=leetcode id=1773 lang=python3
#
# [1773] Count Items Matching a Rule
#

# @lc code=start
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey:  str, ruleValue: str) -> int:
        ans = 0 
        for i in range(len(items)):
            match ruleKey:
                case 'type':
                    ans += 1 if items[i][0] == ruleValue else 0
                case 'color':
                    ans += 1 if items[i][1] == ruleValue else 0
                case 'name':
                    ans += 1 if items[i][2] == ruleValue else 0

        return ans
# @lc code=end

