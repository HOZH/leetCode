#
# @lc app=leetcode id=728 lang=python3
#
# [728] Self Dividing Numbers
#

# @lc code=start


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for num in range(left, right+1):

            temp = num
            flag = True
            while temp:

                current = temp % 10
                if current == 0 or num % current != 0:
                    flag = False
                    break

                temp //= 10

            if flag:
                result.append(num)

        return result


# @lc code=end
