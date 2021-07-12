#
# @lc app=leetcode id=1041 lang=python3
#
# [1041] Robot Bounded In Circle
#

# @lc code=start
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:

        inital_direction = 0
        current_direction = 0

        next_move = ((0, 1), (1, 0), (0, -1), (-1, 0))
        x, y = 0, 0

        for i in instructions:
            if i == 'L':
                current_direction = current_direction - 1 if current_direction > 0 else 3
            elif i == 'R':
                current_direction = current_direction + 1 if current_direction < 3 else 0

            else:
                x += next_move[current_direction][0]
                y += next_move[current_direction][1]

        final_direction = current_direction
        current_direction = 0

        return x == y == 0 or final_direction != inital_direction


# @lc code=end
