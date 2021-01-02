#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#

# @lc code=start

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        row_len = len(board)
        col_len = len(board[0])
        self.used = [[False for _ in range(col_len)] for _ in range(row_len)]
        self.board = board
        found = [False] * len(words)

        def helper(y, x, s):

            if s == '':
                return True

            new_pos = [(y, x - 1), (y, x + 1), (y - 1, x), (y + 1, x)]

            for i in new_pos:

                ny, nx = i

                # valid_ny = ny >= 0 and ny < len(board)
                # valid_nx = nx >= 0 and nx < len(board[0])
                if 0 <= nx < len(board[0]) and 0 <= ny < len(board) and not self.used[ny][nx]:

                    if board[ny][nx] == s[0]:
                        self.used[ny][nx] = True
                        if helper(ny, nx, s[1:]):
                            self.used[ny][nx] = False
                            return True
                        self.used[ny][nx] = False

            return False

        for word_index in range(len(words)):
            # print(board)
            # print(self.used)
            current_word = words[word_index]
            found_current = False
            for i in range(row_len):
                if found_current:
                    break
                for j in range(col_len):
                    # i -> y, j -> x
                    if board[i][j] == current_word[0]:
                        self.used[i][j] = True

                        if helper(i, j, current_word[1:]):
                            found[word_index] = True
                            found_current = True
                            self.used[i][j] = False
                            break

                        self.used[i][j] = False

            ans = []
            # print(found)
            for i in range(len(words)):
                if found[i]:
                    ans.append(words[i])

        return ans


# @lc code=end
