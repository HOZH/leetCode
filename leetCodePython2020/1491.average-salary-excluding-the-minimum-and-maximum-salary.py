#
# @lc app=leetcode id=1491 lang=python3
#
# [1491] Average Salary Excluding the Minimum and Maximum Salary
#

# @lc code=start
class Solution:
    def average(self, salary: List[int]) -> float:

        salary.sort()
        salary = salary[1:-1]

        return sum(salary)/len(salary)


# @lc code=end
