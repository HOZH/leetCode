#
# @lc app=leetcode id=401 lang=python3
#
# [401] Binary Watch
#


class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:

        if num > 8:

            return []

        elif num == 0:

            return ['0:00']

        hours = (1, 2, 4, 8)
        mins = (1, 2, 4, 8, 16, 32)

        result = list()

        for i in range(num+1):

            for_hour = i
            for_min = num-i

            if for_hour > 3 or for_min > 5:
                continue

            hour_list = [0] if for_hour == 0 else list(
                filter(lambda y: y < 12, map(lambda x: sum(x), itertools.combinations(hours, for_hour))))

            min_list = [0] if for_min == 0 else list(
                filter(lambda y: y < 60, map(lambda x: sum(x), itertools.combinations(mins, for_min))))

            for k in hour_list:

                for l in min_list:

                    if l < 10:
                        l = '0'+str(l)

                    temp = str(k)+':'+str(l)
                    result.append(temp)

        from datetime import datetime
        result.sort(key=lambda x: datetime.strptime(x, '%H:%M'))
        return result
