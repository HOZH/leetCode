#
# @lc app=leetcode id=1122 lang=python3
#
# [1122] Relative Sort Array
#

# @lc code=start
from collections import Counter


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

        set2 = set(arr2)

        not_in_arr2 = []
        temp = []

        for i in arr1:
            if i not in set2:
                not_in_arr2.append(i)
            else:
                temp.append(i)

        not_in_arr2.sort()

        counter = Counter(temp)

        ans = []

        for i in arr2:

            ans = ans+counter[i]*[i]

        ans += not_in_arr2

        return ans


# @lc code=end
