#
# @lc app=leetcode id=791 lang=python3
#
# [791] Custom Sort String
#

# @lc code=start
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        in_order, not_in_order = [],[]
        for i in s:
            if i not in order:
                not_in_order.append(i)
            else:
                in_order.append(i)
        in_order.sort(key= lambda x:order.find(x))
        return ''.join(in_order)+''.join(not_in_order)
# @lc code=end

