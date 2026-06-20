#
# @lc app=leetcode id=999 lang=python3
#
# [999] Available Captures for Rook
#

# @lc code=start
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        result = 0
        len_rows = len(board)
        len_cols = len(board[0])
        rock_coordinate = None
        for i in range(len_rows):
            for j in range(len_cols):
                if board[i][j] == "R":
                    rock_coordinate = (i, j)
                    break
        
        result = 0

        # going up
        for i in range(rock_coordinate[0],-1,-1):
            if board[i][rock_coordinate[1]] == "B":
                break
            elif board[i][rock_coordinate[1]] == "p":
                result += 1
                break

        # going down
        for i in range(rock_coordinate[0], len_rows,1):
            if board[i][rock_coordinate[1]] == "B":
                break
            elif board[i][rock_coordinate[1]] == "p":
                result += 1
                break
        
        # going left
        for i in range(rock_coordinate[1],-1,-1):
            if board[rock_coordinate[0]][i] == "B":
                break
            elif board[rock_coordinate[0]][i] == "p":
                result += 1
                break
        
        # going right
        for i in range(rock_coordinate[1], len_cols,1):
            if board[rock_coordinate[0]][i] == "B":
                break
            elif board[rock_coordinate[0]][i] == "p":
                result += 1
                break

        return result

        
# @lc code=end

def numRookCaptures(self, board: List[List[str]]) -> int:
        """
        board = [
            [".",".",".",".",".",".",".","."],
            [".",".",".","p",".",".",".","."],
            [".",".",".","R",".",".",".","p"],
            [".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".","."],
            [".",".",".","p",".",".",".","."],
            [".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".","."]]
        """
        output = 0

        rook_r = 0
        rook_c = 0

        for r, row in enumerate(board):
            for c, col in enumerate(row):
                if col == "R":
                    rook_r = r
                    rook_c = c
                    break
        
        
        r = rook_r
        # up
        while r >= 0:
            tile = board[r][rook_c]
            if tile == "B":
                break
            if tile == "p":
                output += 1
                break
            r -= 1
        # down
        r = rook_r
        while r < len(board):
            tile = board[r][rook_c]
            if tile == "B":
                break
            if tile == "p":
                output += 1
                break
            r += 1
        # left
        c = rook_c
        while c >= 0:
            tile = board[rook_r][c]
            if tile == "B":
                break
            if tile == "p":
                output += 1
                break
            c -= 1
        # right
        c = rook_c
        while c < len(board[0]):
            tile = board[rook_r][c]
            if tile == "B":
                break
            if tile == "p":
                output += 1
                break
            c += 1


        return output
    
    def helper(self, r, c, dir):
        if dir == "up":
            while r >= 0
            r -= 1
        elif dir == "down":
            while r < len(board):
            r += 1
        elif dir == "left":
            c -= 1
        else:
            c += 1
        
        