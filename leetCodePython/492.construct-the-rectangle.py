#
# @lc app=leetcode id=492 lang=python3
#
# [492] Construct the Rectangle
#


class Solution:
    def constructRectangle(self, area: int) -> List[int]:

        if area == 0:
            return []

        base = math.floor(math.sqrt(area))

        while True:

            if area % base == 0:

                temp = area//base

                return(max(base, temp), min(base, temp))
            else:
                base -= 1
