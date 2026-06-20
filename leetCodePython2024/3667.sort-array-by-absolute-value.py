#
# @lc app=leetcode id=3667 lang=python3
#
# [3667] Sort Array By Absolute Value
#

# @lc code=start
class Solution:
    def sortByAbsoluteValue(self, nums: List[int]) -> List[int]:
        return sorted(nums, key=abs)

        mapped = list(map(lambda x: (x, abs(x)), nums))

        mapped.sort(key=lambda x: x[1])

        return list(map(lambda x: x[0], mapped))

# @lc code=end
