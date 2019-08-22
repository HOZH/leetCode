#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#


class Solution:
    def isValid(self, s: str) -> bool:

        # maybe use dict() to compute them pairwisely next time
        deq = collections.deque()

        for i in s:

            if i == "(" or i == "{" or i == "[":

                deq.append(i)
            else:

                length = len(deq)
                if i == ")":
                    if length == 0:
                        return False
                    if deq[-1] != "(":
                        return False
                    else:
                        deq.pop()
                elif i == "}":
                    if length == 0:
                        return False
                    if deq[-1] != "{":
                        return False
                    else:
                        deq.pop()
                elif i == "]":
                    if length == 0:
                        return False

                    if deq[-1] != "[":
                        return False

                    else:
                        deq.pop()

        return True if len(deq) == 0 else False
