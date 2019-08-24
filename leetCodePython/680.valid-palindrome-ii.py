#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#


class Solution:
    def validPalindrome(self, s: str) -> bool:

        def helper(string, flag):
            used = flag

            left = 0

            right = len(string) - 1

            while left < right:

                if string[left] == string[right]:

                    left += 1
                    right -= 1

                else:

                    if not used:

                        used = True

                        delete_left = string[left + 1] == string[right]
                        delete_right = string[left] == string[right - 1]

                        if delete_left and delete_right:

                            a = helper(s[left + 1:right + 1], True)
                            b = helper(s[left:right], True)

                            return a if a else b

                        elif delete_left:

                            left += 2
                            right -= 1

                        elif delete_right:

                            left += 1

                            right -= 2

                        else:

                            return False

                    else:

                        return False

            return True

        return helper(s, False)
