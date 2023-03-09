#
# @lc app=leetcode id=253 lang=python3
#
# [253] Meeting Rooms II
#

# @lc code=start
from heapq import heapify, heappop, heappush


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[1])

        paths = [intervals[0][::-1]]

        for i in range(1, len(intervals)):
            current = intervals[i][::-1]
            temp_list = []
            while len(paths):
                temp = heappop(paths)
                if current[1] < temp[0]:
                    heappush(paths, temp)
                    break
                temp_list.append(temp)
            if not len(temp_list):
                heappush(paths, current)
            else:
                _, temp_list = temp_list[-1], temp_list[:-1]
                for i in temp_list:
                    heappush(paths, i)
                heappush(paths, current)
        return len(paths)

        # for i in range(1, len(intervals)):
        #     added = False
        #     local_max_possible_ending = float('-inf')
        #     place_holder = float('-inf')

        #     for current_path_index in range(len(paths)):
        #         current_path = paths[current_path_index]

        #         current_last_ele = intervals[current_path[-1]]

        #         if intervals[i][0] >= current_last_ele[1]:
        #             if local_max_possible_ending < current_last_ele[1]:
        #                 local_max_possible_ending = current_last_ele[1]
        #                 place_holder = current_path_index
        #                 added = True

        #     if added:
        #         paths[place_holder].append(i)
        #     else:
        #         paths.append([i])

        # return len(paths)


# @lc code=end
