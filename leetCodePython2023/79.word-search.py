#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        possible_starting_index = []

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    possible_starting_index.append((i, j))

        if not len(possible_starting_index):
            return False

        def init_used_matrix(i, j):
            temp = [[False for _ in range(len(board[0]))]
                    for _ in range(len(board))]
            temp[i][j] = True
            return temp

        next_position_offset = ((0, 1), (0, -1), (1, 0), (-1, 0))

        def dfs(i, j, used, current):
            if len(current) == 1 and board[i][j] == current[0]:
                return True
            if current[0] != board[i][j]:
                return False

            for i_offset, j_offset in next_position_offset:
                new_i, new_j = i+i_offset, j+j_offset
                if -1 < new_i < len(board) and -1 < new_j < len(board[0]) and used[new_i][new_j] == False:
                    used[new_i][new_j] = True
                    flag = dfs(new_i, new_j, used, current[1:])
                    if flag:
                        return True
                    else:
                        used[new_i][new_j] = False

        for starting_i, starting_j in possible_starting_index:
            flag = dfs(starting_i, starting_j, init_used_matrix(
                starting_i, starting_j), word)
            if flag:
                return True

        return False


# @lc code=end
