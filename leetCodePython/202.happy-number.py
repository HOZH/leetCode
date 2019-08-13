#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#


class Solution:
    def isHappy(self, n: int) -> bool:

        num = n

        result = -1

        prev_answer = set()
        while True:

            temp_list = list()

            while num != 0:

                temp_list.append(num % 10)

                num = num//10

            result = sum(map(lambda x: x**2, temp_list))

            if result == 1:
                return True

            if result in prev_answer:

                return False

            prev_answer.add(result)

            num = result
