#
# @lc app=leetcode id=1299 lang=python3
#
# [1299] Replace Elements with Greatest Element on Right Side
#

# @lc code=start


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        old_max = arr[-1]
        result = [old_max]

        for i in range(len(arr)-2, 0, -1):
            if arr[i] > old_max:
                old_max = arr[i]
            result.insert(0, old_max)

        return [-1] if len(result) == 1 else result+[-1]


# @lc code=end
