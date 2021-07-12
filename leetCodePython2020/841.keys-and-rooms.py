#
# @lc app=leetcode id=841 lang=python3
#
# [841] Keys and Rooms
#

# @lc code=start


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        if len(rooms) == 1:
            return True

        visited = set()

        def helper(current):

            if current not in visited:

                visited.add(current)
                for i in rooms[current]:
                    helper(i)

        helper(0)

        return len(visited) == len(rooms)

        # return len(remain) == 0
# @lc code=end
