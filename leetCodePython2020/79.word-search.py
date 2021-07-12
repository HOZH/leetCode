#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        row_len = len(board)
        col_len = len(board[0])

        self.used = [[False for _ in range(col_len)] for _ in range(row_len)]

        def helper(x, y, s):

            if s == '':
                return True

            next_positions = [(y-1, x), (y+1, x), (y, x-1), (y, x+1)]
            local_head, local_tail = s[0], s[1:]

            for ny, nx in next_positions:
                # valid_ny = ny >= 0 and ny < len(board)
                # valid_nx = nx >= 0 and nx < len(board[0])
                if (nx >= 0 and nx < col_len) and (ny >= 0 and ny < row_len) and not self.used[ny][nx]:
                    if board[ny][nx] == local_head:
                        self.used[ny][nx] = True
                        if helper(nx, ny, local_tail):
                            return True
                        else:
                            self.used[ny][nx] = False
            return False

        head_letter = word[0]
        tail = word[1:]

        for i in range(row_len):
            for j in range(col_len):
                if board[i][j] == head_letter:

                    self.used[i][j] = True

                    if helper(j, i, tail):
                        return True
                    else:
                        self.used[i][j] = False

        return False


# @lc code=end
