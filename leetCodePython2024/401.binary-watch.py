#
# @lc app=leetcode id=401 lang=python3
#
# [401] Binary Watch
#

# @lc code=start
import itertools

class Solution:
    def readBinaryWatch(self, turnedOn: int):
        if turnedOn > 8:
            return []
        hour_reads, mins_reads = [0, 1, 2, 3, ], [0, 1, 2, 3, 4, 5]
        mins_up_boundary, hours_up_boundary = 60, 12
        ans = []
        for digits_for_hours in range(turnedOn + 1):
            if digits_for_hours > 3:
                continue
            hours = []
            if digits_for_hours == 0:
                hours = [0]
            else:
                combinations = list(itertools.combinations(
                    hour_reads, digits_for_hours))
                for temp in combinations:
                    possibile_result = sum(list(map(lambda x: 2**x, temp)))
                    if possibile_result < hours_up_boundary:
                        hours.append(possibile_result)
            digits_for_mins = turnedOn - digits_for_hours
            if digits_for_mins > 5:
                continue
            mins = []
            if digits_for_mins == 0:
                mins = [0]
            else:
                combinations = list(itertools.combinations(
                    mins_reads, digits_for_mins))
                for temp in combinations:
                    possibile_result = possibile_result = sum(
                        list(map(lambda x: 2**x, temp)))
                    if possibile_result < mins_up_boundary:
                        mins.append(possibile_result)
            for possible_hrs in hours:
                for possible_mins in mins:
                    ans.append(str(possible_hrs) + ':' +
                               ('' if possible_mins > 9 else '0') + str(possible_mins))
        return ans


# @lc code=end
class Solution2:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        if turnedOn > 8:
            return []
        ans = []
        for hr in range(12):
            for mini in range(60):
                count_hr_digits = ("{0:b}".format(hr)).count('1')
                count_min_digits = ("{0:b}".format(mini)).count('1')
                if count_hr_digits + count_min_digits == turnedOn:
                    ans.append(f"{hr}:{'0' if mini < 10 else ''}{mini}")
        return ans