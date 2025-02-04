#
# @lc app=leetcode id=37 lang=python3
#
# [37] Sudoku Solver
#

# @lc code=start
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.rows = [[0 for _ in range(10)] for _ in range(9)]
        self.cols = [[0 for _ in range(10)] for _ in range(9)]
        self.boxes = [[0 for _ in range(10)] for _ in range(9)]

        for i in range(9):
            for j in range(9):
                current = board[i][j]
                if current != '.':
                    temp = int(current)
                    # to get the box position
                    bx = j//3
                    by = i//3

                    self.rows[i][temp] = 1
                    self.cols[j][temp] = 1
                    self.boxes[by*3+bx][temp] = 1

        def helper(board, x, y):
            if y == 9:
                return True

            nx = (x+1) % 9
            ny = y if nx != 0 else y+1

            if board[y][x] != '.':
                return helper(board, nx, ny)

            box_key = x//3 + (y//3)*3

            for i in range(1, 10):
                a = not self.rows[y][i]
                b = not self.cols[x][i]
                c = not self.boxes[box_key][i]

                if a and b and c:
                    self.rows[y][i] = 1
                    self.cols[x][i] = 1
                    self.boxes[box_key][i] = 1

                    board[y][x] = str(i)

                    if helper(board, nx, ny):
                        return True

                    else:
                        self.rows[y][i] = 0
                        self.cols[x][i] = 0
                        self.boxes[box_key][i] = 0

                        board[y][x] = '.'

            return False

        helper(board, 0, 0)

# @lc code=end

