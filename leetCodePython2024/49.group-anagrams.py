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
            key = ''.join(sorted([*i]))
            categories[key].append(i)

        ans = []
        for i in categories.keys():
            ans.append(categories[i])

        return ans

# @lc code=end
