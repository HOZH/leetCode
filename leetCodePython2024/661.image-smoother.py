#
# @lc app=leetcode id=661 lang=python3
#
# [661] Image Smoother
#

# @lc code=start
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        x_len, y_len = len(img[0]), len(img)
        offsets = ((-1,-1),(0,-1),(1,-1),(-1,0),(0,0),(1,0),(-1,1),(0,1),(1,1))
        def helper(x,y): 
            total = 0
            count = 0

            for offset_x, offset_y in offsets:
                new_x,new_y = offset_x+x, offset_y+y
                if 0<=new_x<x_len and 0<=new_y<y_len:
                    total+=img[new_y][new_x]
                    count+=1
            
            return total//count
        
        result = [[0 for _ in range(x_len)] for _ in range(y_len)]

        for i in range(y_len):
            for j in range(x_len):
                result[i][j] = helper(j,i)

        return result
        
# @lc code=end

        for nr in range(max(0, r - 1), min(rows, r + 2)):
            for nc in range(max(0, c - 1), min(cols, c + 2)):

 def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        output = [[0] * len(row) for row in img]

        for r, row in enumerate(img):
            c = 0
            while c < len(row):
                total = self.get_adjacent_values(r, c, img)
                output[r][c] = total
                c += 1
        return output
        

    def get_adjacent_values(self, r, c, img):
        total = img[r][c]
        count = 1
        row = len(img)
        col = len(img[0])
        # vertical and horizontal
        if r - 1 >= 0:
            total += img[r - 1][c]
            count += 1
        if r + 1 < row:
            total += img[r + 1][c]
            count += 1
        if c - 1 >= 0:
            total += img[r][c - 1]
            count += 1
        if c + 1 < col:
            total += img[r][c + 1]
            count += 1
        # diagonals
        if r - 1 >= 0 and c - 1 >= 0:
            total += img[r - 1][c - 1]
            count += 1
        if r - 1 >= 0 and c + 1 < col:
            total += img[r - 1][c + 1]
            count += 1
        if r + 1 < row and c - 1 >= 0:
            total += img[r + 1][c - 1]
            count += 1
        if r + 1 < row and c + 1 < col:
            total += img[r + 1][c + 1]
            count += 1
        return total // count