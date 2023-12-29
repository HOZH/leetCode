#
# @lc app=leetcode id=1105 lang=python3
#
# [1105] Filling Bookcase Shelves
#

# @lc code=start
class Solution:
    def minHeightShelves(self, books, shelf_width: int) -> int:
        dp = [1000**2+1]*len(books)
        for j in range(len(books)):
            max_h_of_current_layer, current_width = 0, 0

            for i in range(j, -1, -1):

                current_width += books[i][0]

                if current_width > shelf_width:
                    break

                max_h_of_current_layer = max(max_h_of_current_layer, books[i][1])
                dp[j] = min(dp[j], (0 if i == 0 else dp[i-1])+max_h_of_current_layer)

        return dp[-1]


# @lc code=end
