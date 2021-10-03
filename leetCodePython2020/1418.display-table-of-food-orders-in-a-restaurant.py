#
# @lc app=leetcode id=1418 lang=python3
#
# [1418] Display Table of Food Orders in a Restaurant
#

# @lc code=start
from collections import defaultdict


class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:

        foods = sorted(list(set(map(lambda x: x[2], orders))))
        header = ['Table']+foods
        food_mapping = dict()
        for i in range(len(foods)):
            food_mapping[foods[i]] = i+1

        tables = dict()

        for current_order in orders:

            current_table = current_order[1]
            current_food = current_order[2]

            if current_table not in tables:
                tables[current_table] = [int(current_table)]+[0]*len(foods)

            tables[current_table][food_mapping[current_food]] += 1

        temp = list(tables.values())
        temp.sort(key=lambda x: x[0])

        for i in range(len(temp)):
            temp[i] = list(map(lambda x: str(x), temp[i]))

        return [header]+temp

# @lc code=end
