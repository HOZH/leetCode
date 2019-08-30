#
# @lc app=leetcode id=859 lang=python3
#
# [859] Buddy Strings
#


class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:

        a_len = len(A)
        b_len = len(B)
        if a_len != b_len:
            return False

        if a_len < 2:

            return False

        if A == B:

            return True if collections.Counter(A).most_common(1)[0][1] > 1 else False

        dic_a, dic_b = dict(), dict()
        for i in range(a_len):

            if A[i] != B[i]:

                dic_a[i] = A[i]
                dic_b[i] = B[i]

        if len(dic_a) != 2:

            return False

        return True if set(dic_a) == set(dic_b) and set(dic_a.values()) == set(dic_b.values()) else False
