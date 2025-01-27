#
# @lc app=leetcode id=286 lang=python3
#
# [286] Walls and Gates
#

# @lc code=start
from collections import deque


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # empty_room = 2 ** 31 - 1
        # next_positions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # def bfs(i, j):
        #     local_shortest = empty_room
        #     queue = deque([(i, j)])
        #     marked = set()
        #     marked.add((i, j))
        #     depth = 1
        #     prev_steps = dict()
        #     final_x, final_y = None, None
        #     final_dis = None
        #     while len(queue):
        #         current_layer_len = len(queue)
        #         while current_layer_len:
        #             x, y = queue.popleft()
        #             for x_offset, y_offset in next_positions:
        #                 new_x, new_y = x + x_offset, y + y_offset
        #                 if 0 <= new_x < len(rooms) and 0 <= new_y < len(rooms[0]) and (new_x, new_y) not in marked and \
        #                         rooms[new_x][new_y] != -1:
        #                     marked.add((new_x, new_y))
        #                     current = rooms[new_x][new_y]
        #                     if current not in {empty_room, -1}:
        #                         if depth + current < local_shortest:
        #                             local_shortest = depth + current
        #                             final_x = new_x
        #                             final_y = new_y
        #                             final_dis = current
        #                     if current != -1:
        #                         next_cell = (new_x,  new_y)
        #                         prev_steps[next_cell] = (x, y)
        #                         queue.append(next_cell)

        #             current_layer_len -= 1
        #         depth += 1
        #         if depth >= local_shortest:
        #             break
        #     rooms[i][j] = local_shortest
        #     current = (final_x, final_y)
        #     count = 0
        #     while True:
        #         if current in prev_steps:
        #             count += 1
        #             prev_x, prev_y = prev_steps[current]
        #             rooms[prev_x][prev_y] = min(
        #                 rooms[prev_x][prev_y], final_dis+count)
        #             current = (prev_x, prev_y)
        #         else:
        #             break

        # for i in range(len(rooms)):
        #     for j in range(len(rooms[0])):
        #         if rooms[i][j] == empty_room:
        #             bfs(i, j)


        next_positions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n = len(rooms), len(rooms[0])

        def bfs():
            queue = deque()
            marked = set()
            depth = 0
            for i in range(len(rooms)):
                for j in range(len(rooms[0])):
                    if rooms[i][j] == 0:
                        queue.append((i, j))
                        marked.add((i, j))

            while len(queue):
                current_layer_len = len(queue)
                while current_layer_len:
                    x, y = queue.popleft()
                    for x_offset, y_offset in next_positions:
                        new_x, new_y = x + x_offset, y + y_offset
                        if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n or rooms[new_x][new_y] == -1 or (new_x, new_y) in marked:
                            continue

                        marked.add((new_x, new_y))
                        rooms[new_x][new_y] = min(
                            rooms[new_x][new_y], depth + 1)
                        queue.append((new_x, new_y))
                    current_layer_len -= 1

                depth += 1

        bfs()

        
# @lc code=end

