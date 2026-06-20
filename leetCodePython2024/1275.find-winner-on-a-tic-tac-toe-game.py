#
# @lc app=leetcode id=1275 lang=python3
#
# [1275] Find Winner on a Tic Tac Toe Game
#

# @lc code=start
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:

        board = [['' for _ in range(3)] for _ in range(3)]
        move_count = 0
        is_player_a = False
        for x, y in moves:
            move_count += 1
            is_player_a = not is_player_a
            board[y][x] = 'A' if is_player_a else 'B'

        def get_outcome():
            center_char = board[1][1] # 'A', 'B'
            top_left, top_right, bottom_left, bottom_right = board[0][0], board[0][2], board[2][0], board[2][2]

            if center_char != '' and any([board[0][1] == center_char == board[2][1], board[1][0] == center_char == board[1][2], top_left == center_char == bottom_right, top_right == center_char == bottom_left]):
                return center_char
            if top_left!= '' and top_left == board[0][1] == top_right:
                return top_left
            if top_right != '' and top_right == board[1][2] == bottom_right:
                return top_right
            if bottom_right != '' and  bottom_right == board[2][1] == bottom_left:
                return bottom_right
            if bottom_left != '' and  bottom_left == board[1][0] == top_left:
                return bottom_left
            
            if move_count == 9:
                return 'Draw'
            
            return 'Pending'
                    
        return get_outcome()
    

[['B', '', 'A']
 ['A', 'A', 'B'],
['B', '', 'A']]




# @lc code=end
def tictactoe(self, moves: List[List[int]]) -> str:
        board_state = [
            [A,0,0],
            [0,A,0],
            [0,0,A]
        ]        

        is_player_a = True
        # moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
        for move in moves:
            if is_player_a:
                board_state[move[0]][move[1]] = 'A'
            else:
                board_state[move[0]][move[1]] = 'B'
            # board_state[move[0], move[1]] = 'A' if is_player_a else 'B'
            is_player_a = not is_player_a

        winner_state = self.get_winner_state()

        for win in winner_state:
            # did A win:
            cell0 = win[0] #[0,0]
            cell1 = win[1] #[0,1]
            cell2 = win[2] #[0,2]

            # board_state []

            board_state_cell0 = board_state[cell0[0]][cell0[1]] # A
            board_state_cell1 = board_state[cell1[0]][cell1[1]] # 0
            board_state_cell2 = board_state[cell2[0]][cell2[1]] # 0


            if board_state_cell0 == 'A' and board_state_cell1 == 'A' and board_state_cell2 == 'A':
                return 'A'
            elif board_state_cell0 == 'B' and board_state_cell1 == 'B' and board_state_cell2 == 'B':
                return 'B'
        
        if len(moves) < 9:
            return 'Pending'
        else:
            return 'Draw'

        
def get_winner_state(self):
    return [ 
        [[0,0], [0,1], [0,2]],
        [[1,0], [1,1], [1,2]],
        [[2,0], [2,1], [2,2]],
        [[0,0], [1,0], [2,0]],
        [[0,1], [1,1], [2,1]],
        [[0,2], [1,2], [2,2]],
        [[0,0], [1,1], [2,2]],
        [[0,2], [1,1], [2,0]],
    ]

    [
        [1,1,1],
        [0,0,0],
        [0,0,0],
    ],
    [
        [0,0,0],
        [1,1,1],
        [0,0,0],
    ]
