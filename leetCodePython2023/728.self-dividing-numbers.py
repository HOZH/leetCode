#
# @lc app=leetcode id=728 lang=python3
#
# [728] Self Dividing Numbers
#

# @lc code=start
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for i in range(left, right+1):
            flag = True
            str_i = str(i)
            for j in str_i:
                num_j = int(j)
                if num_j == 0 or i % num_j != 0:
                    flag = False
                    break
            if flag:
                result.append(i)

        return result


# @lc code=end
