#
# @lc app=leetcode id=1431 lang=python3
#
# [1431] Kids With the Greatest Number of Candies
#

# @lc code=start


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        threshold = max(candies) - extraCandies

        # return list(map(lambda x: True if x >= threshold else False, candies))

        result = []
        for i in candies:
            if i>=threshold:
                result.append(True)
            else:
                result.append(False)


        return result


# @lc code=end
