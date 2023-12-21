#
# @lc app=leetcode id=1295 lang=python3
#
# [1295] Find Numbers with Even Number of Digits
#

# @lc code=start
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return list(map(lambda i: True if len(str(i)) % 2 == 0 else False, nums)).count(True)

# @lc code=end
