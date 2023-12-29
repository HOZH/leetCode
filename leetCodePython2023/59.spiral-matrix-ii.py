#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[float('inf') for _ in range(n)] for _ in range(n)]
        current_action_index = 0
        actions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        val = 1
        y, x = 0, 0
        ans[0][0] = 1

        while val < n**2:
            val += 1
            y_offset, x_offset = actions[current_action_index]
            new_y, new_x = y+y_offset, x+x_offset
            if -1 < new_y < n and -1 < new_x < n and ans[new_y][new_x] == float('inf'):
                pass
            else:
                current_action_index = (current_action_index+1) % 4
                y_offset, x_offset = actions[current_action_index]
                new_y, new_x = y+y_offset, x+x_offset

            ans[new_y][new_x] = val

            y, x = new_y, new_x

        return ans


# @lc code=end
