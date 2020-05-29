#
# @lc app=leetcode id=1295 lang=python3
#
# [1295] Find Numbers with Even Number of Digits
#

# @lc code=start


class Solution:
    def findNumbers(self, nums: List[int]) -> int:

        return len(list(filter(lambda y: len(y) % 2 == 0, map(lambda x: str(x), nums))))


# @lc code=end
