#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#


class Solution:
    def firstUniqChar(self, s: str) -> int:


        count = collections.Counter(s)



        for index, char in enumerate(s):

            if count[char] == 1:

                return index

        return -1

        # length = len(s)

        # if length == 0:
        #     return -1
        # if length == 1:
        #     return 0

        # lala = min(s, key=s.count)
        # # lala = '1'

        # return -1 if s.count(lala) != 1 else s.find(lala)
