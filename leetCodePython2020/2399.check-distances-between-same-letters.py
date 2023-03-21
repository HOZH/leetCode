#
# @lc app=leetcode id=2399 lang=python3
#
# [2399] Check Distances Between Same Letters
#

# @lc code=start
from collections import defaultdict


class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        distance_dict = defaultdict(int)
        appeared = set()
        for i in range(len(s)):
            appeared.add(s[i])
            if distance_dict[s[i]] != 0:
                # padding = 1
                distance_dict[s[i]] += 1
            distance_dict[s[i]] = (i+1)-distance_dict[s[i]]

        for i in appeared:
            if distance[ord(i)-97] != distance_dict[i]:
                return False

        return True


# @lc code=end
