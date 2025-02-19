#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        categories = defaultdict(list)
        for i in strs:
            # by counter #1#2#3#0#0#0...#0
            # key = ''.join(sorted([*i]))
            key = ''.join(sorted(list(i)))
            categories[key].append(i)

        ans = []
        for i in categories.keys():
            ans.append(categories[i])

        return ans

# @lc code=end
