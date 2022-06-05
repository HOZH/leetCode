#
# @lc app=leetcode id=260 lang=python3
#
# [260] Single Number III
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        temp = set()
        for i in nums:
            if i in temp:
                temp.remove(i)
            else:
                temp.add(i)
        return temp
        
# @lc code=end

