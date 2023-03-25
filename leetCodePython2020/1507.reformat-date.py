#
# @lc app=leetcode id=1507 lang=python3
#
# [1507] Reformat Date
#

# @lc code=start
class Solution:
    def reformatDate(self, date: str) -> str:

        bag = date.split(' ')
        month_dict = {"Jan": '01', "Feb": '02', "Mar": '03', "Apr": '04', "May": '05', "Jun": '06',
                      "Jul": '07', "Aug": '08', "Sep": '09', "Oct": '10', "Nov": '11', "Dec": '12'}
        day = list(filter(lambda x: x.isdigit(), [*bag[0]]))
        day = (day[0]+day[1]) if len(day) == 2 else '0'+day[0]
        return bag[2]+'-'+month_dict[bag[1]]+'-'+day

# @lc code=end
