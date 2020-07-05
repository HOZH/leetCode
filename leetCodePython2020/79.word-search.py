#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row_len = len(board[0])
        col_len = len(board)
        self.used = [[False for j in range(row_len)]
                     for i in range(col_len)]

        def helper(board, x, y, s):
            if s == '':
                return True

            next_positions = [(y-1, x), (y+1, x), (y, x-1), (y, x+1)]

            for i in next_positions:

                ny, nx = i
                # valid_ny = ny >= 0 and ny < len(board)
                # valid_nx = nx >= 0 and nx < len(board[0])
                if (nx >= 0 and nx < len(board[0])) and (ny >= 0 and ny < len(board)) and not self.used[ny][nx]:
                    if board[ny][nx] == s[0]:
                        self.used[ny][nx] = True

                        if helper(board, nx, ny, s[1:]):
                            return True
                        else:
                            self.used[ny][nx] = False

            return False

        for i in range(col_len):
            for j in range(row_len):
                if board[i][j] == word[0]:

                    self.used[i][j] = True

                    if helper(board, j, i, word[1:]):
                        return True
                    else:
                        self.used[i][j] = False

        return False


# @lc code=end
