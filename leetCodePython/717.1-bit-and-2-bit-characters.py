#
# @lc app=leetcode id=717 lang=python3
#
# [717] 1-bit and 2-bit Characters
#


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:

        zero, one, two, three, empty = '0', '1', '10', '11', ''

        if len(bits) == 1:

            return True

        elif bits[-2] == 0:

            return True

        else:

            a = empty.join(list(map(lambda x: str(x), bits)))

            while True:

                remain_len = len(a)

                if remain_len == 1:

                    return True

                elif remain_len == 0:

                    return False

                elif a[0] == zero:

                    a = a[1:]
                    continue

                a = a.replace(three, empty, 1) if a[1] == one else a.replace(
                    two, empty, 1)
