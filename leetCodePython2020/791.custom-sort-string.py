#
# @lc app=leetcode id=791 lang=python3
#
# [791] Custom Sort String
#

# @lc code=start
from collections import Counter


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # 2023 revision
        counter = Counter(s)
        ans = ''
        for i in s:
            if i not in order:
                ans += i
        for i in order:
            ans += i*counter[i]
        return ans
        # in_order, not_in_order = [],[]
        # order_set = set(order)
        # for i in s:
        #     if i not in order_set:
        #         not_in_order.append(i)
        #     else:
        #         in_order.append(i)
        # in_order.sort(key= lambda x:order.find(x))
        # return ''.join(in_order)+''.join(not_in_order)
# @lc code=end
