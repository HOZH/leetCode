#
# @lc app=leetcode id=841 lang=python3
#
# [841] Keys and Rooms
#

# @lc code=start
from collections import deque


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        available_rooms = {0}
        visited = [False]*len(rooms)
        queue = deque([0])
        while len(queue):
            current_layer_len = len(queue)
            while current_layer_len:
                current_room = queue.pop()
                if visited[current_room]:
                    current_layer_len -= 1
                    continue
                visited[current_room] = True
                available_rooms |= set(rooms[current_room])
                for i in rooms[current_room]:
                    if visited[i] == False:
                        queue.append(i)
                current_layer_len -= 1
        return len(available_rooms) == len(rooms)


# @lc code=end
