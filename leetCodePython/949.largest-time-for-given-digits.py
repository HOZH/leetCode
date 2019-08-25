#
# @lc app=leetcode id=949 lang=python3
#
# [949] Largest Time for Given Digits
#


class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:

        def helper(num, A):

            string = ""

            counter = collections.Counter(A)

            if not counter[num]:
                return ""

            if counter[num]:

                string += str(num)

                counter[num] -= 1

                key = 3 if num == 2 else 9
                for j in range(key, -1, -1):

                    if counter[j]:
                        counter[j] -= 1

                        string += str(j) + ":"
                        break

                    if j == 0:
                        return ""

                for j in range(5, -1, -1):

                    if counter[j]:
                        string += str(j)
                        counter[j] -= 1
                        break

                    if j == 0:
                        return ""

                for j in range(9, -1, -1):

                    if counter[j]:
                        string += str(j)
                        counter[j] -= 1
                        break

                    if j == 0:
                        return ""

                return string

            return ""

        return max(helper(0, A), helper(1, A), helper(2, A))
