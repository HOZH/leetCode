#
# @lc app=leetcode id=2553 lang=python3
#
# [2553] Separate the Digits in an Array
#

# @lc code=start
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        temp = []
        for i in nums:
            temp.extend([*str(i)])

        return list(map(lambda x: int(x), [item for sublist in temp for item in sublist]))

# @lc code=end
