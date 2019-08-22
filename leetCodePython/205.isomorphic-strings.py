#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        len_s = len(s)
        len_t = len(t)

        dic_s = dict()
        dic_t = dict()

        if len_s != len_t:
            return False

        elif len_s == 0:

            return True

        prev_s, prev_t, count_s, count_t = s[0], t[0], 1, 1
        dic_s[prev_s] = [0]
        dic_t[prev_t] = [0]
        for i in range(1, len_s):

            if s[i] == prev_s:
                count_s += 1
                dic_s[prev_s].append(i)

            else:
                count_s = 1
                if s[i] not in dic_s:
                    dic_s[s[i]] = [i]
                else:
                    dic_s[prev_s].append(i)

                prev_s = s[i]

            if t[i] == prev_t:
                count_t += 1
                dic_t[prev_t].append(i)

            else:
                count_t = 1
                if t[i] not in dic_t:
                    dic_t[t[i]] = [i]
                else:
                    dic_t[prev_t].append(i)
                prev_t = t[i]

            if count_s != count_t or dic_s[prev_s] != dic_t[prev_t]:
                return False

        return True

        # or I could replace chars in both string with unified marks like(a,b,c...)
