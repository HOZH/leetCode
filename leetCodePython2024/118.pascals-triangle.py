#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]

        if numRows == 1:
            return ans

        for i in range(1, numRows):
            prev_layer_index = i-1
            temp = []
            for j in range(0, i+1):
                if j == 0 or j == i:
                    temp.append(1)
                else:
                    temp.append(ans[prev_layer_index]
                                [j-1] + ans[prev_layer_index][j])

            ans.append(temp)

        return ans


# @lc code=end
