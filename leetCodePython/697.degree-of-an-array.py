#
# @lc app=leetcode id=697 lang=python3
#
# [697] Degree of an Array
#
class Solution:

    def position_last(self, x, s):

        # for i, v in enumerate(reversed(s)):
        #     if v == x:
        #         return len(s) - i - 1
        return next(i for i, j in list(enumerate(s))[::-1] if j == x)

    def findShortestSubArray(self, nums):

        len_nums = len(nums)

        if len(set(nums)) == len_nums:
            return 1

        max_list = list()
        temp_list = list()
        max_list.append(max(set(nums), key=nums.count))

        


        temp_list = list(filter(lambda x: x != max_list[0], nums))


        max_count = len_nums - len(temp_list)


        

        while True:

            if len(temp_list) > 0:

                temp = max(set(temp_list), key=temp_list.count)

                temp_list1 = list(filter(lambda x: x != temp, temp_list))

                if len(temp_list) - len(temp_list1) == max_count:

                    max_list.append((temp))
                    temp_list = list(filter(lambda x: x != temp, temp_list))

                else:
                    break

            else:
                break

        shortest = list()

        for i in max_list:
            current = self.position_last(i, nums) - nums.index(i) + 1

            shortest.append(current)

        return min(shortest)
