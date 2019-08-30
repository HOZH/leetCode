#
# @lc app=leetcode id=1154 lang=python3
#
# [1154] Day of the Year
#


class Solution:
    def dayOfYear(self, date: str) -> int:

        dates = date.split("-")

        year, month, day = int(dates[0]), int(dates[1]), int(dates[2])

        dic = dict()

        if ((year % 400 == 0)or ((year % 4 == 0) and (year % 100 != 0))):

            dic[2] = 29

        else:

            dic[2] = 28

        dic[1] = 31
        dic[3] = 31
        dic[5] = 31
        dic[7] = 31
        dic[8] = 31
        dic[10] = 31
        dic[12] = 31
        dic[4] = 30
        dic[6] = 30
        dic[9] = 30
        dic[11] = 30

        days = 0

        for i in range(1, month):

            days += dic[i]

        return days+day
