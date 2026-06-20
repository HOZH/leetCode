#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#

# @lc code=start
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()

        # Step 1). build the initial set of rotten oranges
        fresh_oranges = 0
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_oranges += 1
        if fresh_oranges == 0 and len(queue) == 0:
            return 0
        visited = set()


        # Step 2). start the rotting process via BFS
        minutes_elapsed = -1
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        while queue:
            current_layer_len = len(queue)
            while current_layer_len>0:
                row, col = queue.popleft()
                for d in directions:
                    neighbor_row, neighbor_col = row + d[0], col + d[1]
                    if (neighbor_row,neighbor_col) not in visited and ROWS > neighbor_row >= 0 and COLS > neighbor_col >= 0:
                        if grid[neighbor_row][neighbor_col] == 1:
                            # this orange would be contaminated
                            grid[neighbor_row][neighbor_col] = 2
                            fresh_oranges -= 1
                            # this orange would then contaminate other oranges
                            queue.append((neighbor_row, neighbor_col))
                        visited.add((neighbor_row,neighbor_col))

                current_layer_len-=1
            minutes_elapsed += 1


        # return elapsed minutes if no fresh orange left
        return minutes_elapsed if fresh_oranges == 0 else -1
    
    def orangesRotting_temp(self, grid: List[List[int]]) -> int:

        def helper(x,y):
            """
            return -1 if this orange cannot rot
            return 1 if this orange will rot next round
            return 0 if this orange will not rot next round
            """
            directions = [(0,1),(1,0),(-1,0),(0,-1)]
            adjacent_orange_count = 0
            for direction in directions:
                new_x = x + direction[0]
                new_y = y + direction[1]
                if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]):
                    if grid[new_x][new_y] == 0:
                        continue
                    if grid[new_x][new_y] == 1:
                        adjacent_orange_count +=1
                        continue

                    if grid[new_x][new_y] == 2:
                        return 1
            if adjacent_orange_count == 0:
                return -1
            else:
                return 0
        mins=0

        fresh_orange_indexes = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh_orange_indexes.add( (i,j) )
        initial_fresh_orange_count = len(fresh_orange_indexes)

        while True:
            initial_fresh_orange_count = len(fresh_orange_indexes)
            if initial_fresh_orange_count == 0:
                return mins 
            
            pending_rotten_indexes = set()
            for i,j in fresh_orange_indexes:
                result = helper(i,j)
                if result == -1:
                    return -1
                if result == 1:
                    pending_rotten_indexes.add((i,j))
                if result == 0:
                    continue
            for i,j in pending_rotten_indexes:
                grid[i][j]=2
            fresh_orange_indexes-=pending_rotten_indexes
            after_fresh_orange_count = len(fresh_orange_indexes)
            if initial_fresh_orange_count == after_fresh_orange_count:
                return -1
            
            mins+=1
        
# @lc code=end

