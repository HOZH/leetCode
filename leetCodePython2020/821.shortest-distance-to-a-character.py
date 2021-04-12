#
# @lc app=leetcode id=821 lang=python3
#
# [821] Shortest Distance to a Character
#

# @lc code=start
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:

        limit = 10 ** 5
        length = len(s)
        res = [limit] * length

        e = -1
        for i in range(length):
            a = s[i]
            if s[i] == c:
                res[i] = 0
                e = i
            else:
                if e != -1:
                    res[i] = i - e
                else:
                    res[i] = -1

        e = -1
        for i in range(length - 1, -1, -1):
            a = s[i]

            if s[i] == c:
                e = i
            else:

                res[i] = min([limit if res[i] == -1 else res[i],
                              limit if e == -1 else e - i])

        return res


# @lc code=end
