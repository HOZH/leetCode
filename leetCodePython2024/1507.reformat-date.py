#
# @lc app=leetcode id=1507 lang=python3
#
# [1507] Reformat Date
#

# @lc code=start
class Solution:
    def reformatDate(self, date: str) -> str:
        day_raw, month_raw, year = date.split(' ')
        month_mapping = {"Jan": '01', "Feb": '02', "Mar": '03', "Apr": '04', "May": '05',
                         "Jun": '06', "Jul": '07', "Aug": '08', "Sep": '09', "Oct": '10', "Nov": '11', "Dec": '12'}
        # month_mapping = {
        #     month: f"{i:02d}" for i, month in enumerate(months, start=1)}
        day_without_postfix = day_raw[:-2]
        if len(day_without_postfix) == 1:
            day = '0'+day_without_postfix
        else:
            day = day_without_postfix

        return '-'.join([year, month_mapping[month_raw], day])

# @lc code=end


dict = {"Jan", "Feb", "Mar", "Apr", "May", "Jun",
        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"}
"20th Oct 2052" -> ["20th", "Oct",]
Output: "2052-10-20"

"20th" - > 20
"6th" -> 6
