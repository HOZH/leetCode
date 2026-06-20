#
# @lc app=leetcode id=766 lang=python3
#
# [766] Toeplitz Matrix
#

# @lc code=start
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        visited = set()
        y_len, x_len = len(matrix), len(matrix[0])

        def is_qualified(y, x):
            if (y, x) in visited:
                return True
            input_val = matrix[y][x]
            new_x = x
            for new_y in range(y+1, y_len):
                new_x += 1
                if new_x < x_len:
                    if matrix[new_y][new_x] != input_val:
                        return False
                    else:
                        visited.add((new_y, new_x)) 
                else:
                    break

            return True

        for i in range(y_len-1):
            for j in range(x_len-1):
                if not is_qualified(i, j):
                    return False

        return True
# @lc code=end


 def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        self.visited = [[False] * len(row) for row in matrix]
        
        for i, row in enumerate(matrix):
            c = 0
            while c < len(row):
                value = self.update_diag_values(i, c, matrix)
                if value == False:
                    return False
                c += 1

        return True


    def update_diag_values(self, r, c, matrix):
        current = matrix[r][c]
        row = len(matrix)
        col = len(matrix[0])
        output = True
        while r < row and c < col:
            if self.visited[r][c]:

                continue
            else:
                 if matrix[r][c] != current:
                    output = False
                    self.visited[r][c] = True
                    return False
            # if not self.visited[r][c]:
            #     if matrix[r][c] != current:
            #         output = False
            #         break
            self.visited[r][c] = True
            r += 1
            c += 1
        return True
    

    [ [1,2,3,4],
      [5,1,2,3],
      [9,5,1,2]
      ]

    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m -1):
            for j in range(n -1):
                if matrix[i][j] != matrix[i+1][j+1]:
                    return False

        return True