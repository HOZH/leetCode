#
# @lc app=leetcode id=1431 lang=python3
#
# [1431] Kids With the Greatest Number of Candies
#

# @lc code=start
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        current_max_candy_count = max(candies)
        ans = []
        for i in range(len(candies)):
            ans.append(candies[i]+extraCandies >= current_max_candy_count)

        return ans


# @lc code=end
