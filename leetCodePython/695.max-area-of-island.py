#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        # bfs

        h_len = len(grid[0])
        v_len = len(grid)

        max_count = 0

        visited = set()

        for i in range(h_len):

            for j in range(v_len):
                if (i, j) in visited:
                    continue

                visited.add((i, j))

                if grid[j][i] == 0:
                    continue

                current_count = 1

                queued = collections.deque()

                queued.append((i, j))

                while len(queued) != 0:

                    current = queued.popleft()

                    h, v = current[0], current[1]

                    if h - 1 >= 0:

                        if grid[v][h - 1] != 0:

                            if (h - 1, v) not in visited:
                                queued.append((h - 1, v))
                                visited.add((h - 1, v))
                                current_count += 1

                    if h + 1 < h_len:

                        if grid[v][h + 1] != 0:

                            if (h + 1, v) not in visited:
                                queued.append((h + 1, v))
                                visited.add((h + 1, v))
                                current_count += 1

                    if v - 1 >= 0:

                        if grid[v - 1][h] != 0:

                            if (h, v - 1) not in visited:
                                queued.append((h, v - 1))
                                visited.add((h, v - 1))
                                current_count += 1

                    if v + 1 < v_len:

                        if grid[v + 1][h] != 0:

                            if (h, v + 1) not in visited:
                                queued.append((h, v + 1))
                                visited.add((h, v + 1))
                                current_count += 1

                if current_count > max_count:
                    max_count = current_count

        return max_count
