#
# @lc app=leetcode id=744 lang=python3
#
# [744] Find Smallest Letter Greater Than Target
#


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        if target >= letters[-1]:
            return letters[0]

        else:

            # binary search logn

            left = 0

            right = len(letters)-1

            pivot = len(letters)//2

            while True:

                if left >= right:

                    return letters[(left+right)//2]

                elif target < letters[pivot]:

                    right = pivot

                else:

                    left = pivot+1

                pivot = (right-left)//2+left

            # linear search n
