#
# @lc app=leetcode id=999 lang=python3
#
# [999] Available Captures for Rook
#

# @lc code=start

from collections import deque


class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        y, x = next((i, j) for j in range(8)
                    for i in range(8) if board[i][j] == 'R')
        row = ''.join(board[y][j] for j in range(8) if board[y][j] != '.')
        col = ''.join(board[i][x] for i in range(8) if board[i][x] != '.')
        return sum('Rp' in s for s in (row, col)) + sum('pR' in s for s in (row, col))
        # r = tuple()
        # found = False
        # ans = 0
        # row_len, col_len = len(board), len(board[0])
        # processed = set()
        # for i in range(row_len):
        #     for j in range(col_len):

        #         if board[i][j] == 'R':
        #             r = (i, j)
        #             found = True
        #             break
        #     if found:
        #         break

        # moves = ((0, 1), (0, -1), (1, 0), (-1, 0))

        # queue = deque([r])

        # while len(queue):

        #     current_queue_len = len(queue)

        #     while current_queue_len:

        #         current = queue.pop()

        #         for y, x in moves:
        #             new_y, new_x = y+current[0], x+current[1]
        #             if 0 <= new_y < row_len and 0 <= new_x < col_len and (new_y, new_x) not in processed and board[new_y][new_x] != 'board':
        #                 queue.appendleft((new_y, new_x))
        #                 if board[new_y][new_x] == 'p':
        #                     ans += 1

        #                 processed.add((new_y, new_x))

        #         current_queue_len -= 1

        # return ans


# @lc code=end
