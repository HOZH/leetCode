#
# @lc app=leetcode id=1773 lang=python3
#
# [1773] Count Items Matching a Rule
#

# @lc code=start
from collections import defaultdict


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:

        types, colors, names = defaultdict(
            list), defaultdict(list), defaultdict(list)

        for i in range(len(items)):
            current = items[i]
            types[current[0]].append(i)
            colors[current[1]].append(i)
            names[current[2]].append(i)

        menu = dict()
        menu['type'] = types
        menu['color'] = colors
        menu['name'] = names

        return len(menu[ruleKey][ruleValue])

# @lc code=end
