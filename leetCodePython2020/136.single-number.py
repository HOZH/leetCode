#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        temp = set()
        for i in nums:

            if i not in temp:
                temp.add(i)
            else:
                temp.remove(i)

        return temp.pop()
# @lc code=end
