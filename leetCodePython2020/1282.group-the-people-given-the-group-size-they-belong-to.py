#
# @lc app=leetcode id=1282 lang=python3
#
# [1282] Group the People Given the Group Size They Belong To
#

# @lc code=start
from collections import defaultdict


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:

        groups = defaultdict(list)

        for i in range(len(groupSizes)):
            current_category = groups[groupSizes[i]]
            if len(current_category) == 0 or len(current_category[-1]) == groupSizes[i]:
                current_category.append([i])

            else:
                current_category[-1].append(i)

        ans = []
        for i in groups.values():
            for j in i:
                ans.append(j)

        return ans


# @lc code=end
