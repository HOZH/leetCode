#
# @lc app=leetcode id=412 lang=python3
#
# [412] Fizz Buzz
#

# @lc code=start
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:

        answer = []

        for i in range(1, n+1):

            temp = ''
            if i % 3 == 0:
                temp += 'Fizz'

            if i % 5 == 0:
                temp += 'Buzz'

            if not len(temp):
                temp = str(i)

            answer.append(temp)

        return answer

# @lc code=end
