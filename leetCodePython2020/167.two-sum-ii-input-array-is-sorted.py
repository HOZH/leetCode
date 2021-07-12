#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input array is sorted
#

# @lc code=start


class Solution:
    def twoSum_for_non_negative_nums(self, numbers: List[int], target: int) -> List[int]:
        pt1, pt2 = 0, 0
        length = len(numbers)
        temp = 0

        # assign pt1 to biggest number in arr that small than target
        while pt1 < length and numbers[pt1] < target:

            temp = pt1
            pt1 += 1
        pt1 = temp

        while True:

            while pt2 < pt1:

                if numbers[pt2]+numbers[pt1] == target:
                    if pt1 != pt2:
                        return [pt2+1, pt1+1]

                else:
                    pt2 += 1

            pt1 -= 1

    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        pt1, pt2 = 0, len(numbers)-1

        while pt1 < pt2:
            s = numbers[pt1]+numbers[pt2]

            if s > target:
                pt2 -= 1
            elif s < target:
                pt1 += 1
            else:
                return [pt1+1, pt2+1]


# @lc code=end
