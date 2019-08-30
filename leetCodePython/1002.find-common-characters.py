#
# @lc app=leetcode id=1002 lang=python3
#
# [1002] Find Common Characters
#


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:

        #or use counter for a better performance

        length = len(min(A, key=lambda x: len(x)))

        lis = list()

        for _ in range(length):
            for i in range(97, 123):

                current = chr(i)
                if all(x.__contains__(current) for x in A):

                    lis.append(current)

                    A = list(map(lambda x: x.replace(current, "", 1), A))

                    break

        return lis
