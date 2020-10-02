#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#

# @lc code=start


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        result = [[0] * n for _ in range(n)]
        # right -> 0 down ->1 left ->2 up -> 3
        direction = ((0, 1), (-1, 0), (0, -1), (1, 0))
        current_y, current_x = 0, 0
        next_direction = 0
        end = n ** 2
        for i in range(1, end + 1):

            result[current_y][current_x] = i
            new_y, new_x = current_y + \
                direction[next_direction][0], current_x + \
                direction[next_direction][1]

            while not (0 <= new_y < n and 0 <= new_x < n and result[new_y][new_x] == 0):
                if i == end:
                    break
                next_direction += 1
                next_direction %= 4
                new_y, new_x = current_y + \
                    direction[next_direction][0], current_x + \
                    direction[next_direction][1]

            current_y, current_x = current_y + \
                direction[next_direction][0], current_x + \
                direction[next_direction][1]

        return result

# @lc code=end
