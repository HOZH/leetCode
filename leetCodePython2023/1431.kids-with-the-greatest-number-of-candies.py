#
# @lc app=leetcode id=1431 lang=python3
#
# [1431] Kids With the Greatest Number of Candies
#

# @lc code=start
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        threshold = max(candies)
        return list(map(lambda x: True if x+extraCandies >= threshold else False, candies))

# @lc code=end
