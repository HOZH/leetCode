#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#

# @lc code=start

from functools import lru_cache


class Solution:

    def partition_temp(self, s: str):
        if len(s) == 0:
            return [[]]
        record = dict()
        dp = [[]] * len(s)
        dp[0] = [[s[0]]]
        record[s[0]] = [[s[0]]]
        record[''] = [[]]

        for i in range(1, len(s)):
            temp = []
            for j in dp[i - 1]:
                temp.append(j + [s[i]])

            t = s[i]
            for k in range(i - 1, -1, -1):
                t = s[k] + t
                if t == t[::-1]:
                    # print(record[s[:k]])
                    # print(k,record[s[:k]]==dp[k-1])
                    # for l in record[s[:k]]:

                    if k == 0:
                        temp.append([t])
                    else:
                        for l in dp[k - 1]:
                            temp.append(l + [t])

            dp[i] = temp
            record[s[:i + 1]] = temp

        return dp[-1]

    def partition_rec(self, s: str):

        d = dict()
        palindrome = set()

        def helper(sub):
            result = []
            if len(sub) == 0:
                return [[]]
            if len(sub) == 1:
                d[sub] = [[sub]]
                return [[sub]]
            temp = ''
            for i in range(len(sub)):
                temp += sub[i]
                if temp in palindrome or temp == temp[::-1]:

                    palindrome.add(temp)

                    local_sub = [temp]
                    if sub[i + 1:] in d:
                        sub_result = d[sub[i + 1:]]
                    else:
                        sub_result = helper(sub[i + 1:])
                        d[sub[i + 1:]] = sub_result

                    for j in sub_result:
                        result.append(local_sub[:] + j)

            d[sub] = result
            return result

        return helper(s)

    @lru_cache(None)
    def partition(self, s: str):

        if len(s) == 0:
            return tuple()
        if len(s) == 1:
            return tuple((s,))

        result = []
        if s == s[::-1]:
            result.append([s])
        for i in range(1, len(s) + 1):
            temp = s[:i]
            p = temp == temp[::-1]
            if p:
                temp_tuple = self.partition(s[i:])
                for j in temp_tuple:
                    result.append([temp] + list(j))
        return tuple(result)

# @lc code=end
