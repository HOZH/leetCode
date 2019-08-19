#
# @lc app=leetcode id=299 lang=python3
#
# [299] Bulls and Cows
#


class Solution:
    def getHint(self, secret: str, guess: str) -> str:

        a, b, a_temp, b_temp = 0, 0, "", ""

        for i in range(len(secret)):

            if secret[i] == guess[i]:
                a += 1
            else:
                a_temp += secret[i]
                b_temp += guess[i]

        for i in b_temp:

            if i in a_temp:
                a_temp = a_temp.replace(i, "", 1)
                b += 1

        return str(a)+"A"+str(b)+"B"
