#
# @lc app=leetcode id=599 lang=python3
#
# [599] Minimum Index Sum of Two Lists
#

# @lc code=start
from collections import defaultdict


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        words_in_list_1 = set(list1)
        bag = defaultdict(int)
        for i in range(len(list2)):
            current = list2[i]
            if current in words_in_list_1:
                bag[current] = i
        for i in range(len(list1)):
            current = list1[i]
            if current in bag:
                bag[current] += i

        min_index_sum = min(bag.values())
        ans = []
        for key, val in bag.items():
            if val == min_index_sum:
                ans.append(key)

        return ans

# @lc code=end
