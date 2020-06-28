#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start


class Solution:

    def findMedianSortedArrays(self, nums1, nums2) -> float:

        len1, len2 = len(nums1), len(nums2)
        # fixme fix the logic here
        if len1 == 0:

            if len2 % 2 == 0:
                return (nums2[len2 // 2] + nums2[len2 // 2 - 1]) / 2
            else:
                return nums2[len2 // 2]

        elif len2 == 0:
            if len1 % 2 == 0:
                return (nums1[len1 // 2] + nums1[len1 // 2 - 1]) / 2
            else:
                return nums1[len1 // 2]

        l1, l2, r1, r2 = 0, 0, len1 - 1, len2 - 1

        i1, i2 = -1, -1

        pivot1 = l1 + (r1 - l1) // 2

        left1 = nums1[:pivot1]
        right1 = nums1[pivot1:]
        # print(left1)
        # print(right1)
        # print(nums1[pivot1])

        while l2 <= r2:

            pivot2 = l2 + (r2 - l2) // 2

            if nums2[pivot2] == nums1[pivot1]:
                i2 = pivot2
                break

            elif nums2[pivot2] < nums1[pivot1]:
                l2 = pivot2 + 1
            else:
                r2 = pivot2 - 1

        i2 = i2 if i2 != -1 else l2
        left2 = nums2[:i2]
        right2 = nums2[i2:]

        len_left, len_right = len(
            left1) + len(left2), len(right1) + len(right2)

        # print(len_left, len_right)
        #
        # print(left1, right1)
        # print(left2, right2)
        # return None

        while abs(len_left - len_right) > 1:

            if len_left < len_right:

                if len(right1) == 0:
                    i2 = 0 + (len(right2 - 1) - 0) // 2

                    # fixme fixed
                    left2, right2 = left2 + right2[:i2 + 1], right2[i2 + 1:]

                elif len(right2) == 0:
                    pivot1 = 0 + (len(right1 - 1) - 0) // 2

                    # fixme fixed
                    left1, right1 = left1 + right1[:pivot1 + 1], right1[pivot1 + 1:]

                elif right2[0] == right1[0]:
                    left1, right1 = left1 + right1[:1], right1[1:]

                else:

                    if right1[0] < right2[0]:
                        pivot1 = 0 + (len(right1) - 1 - 0) // 2

                        l2, r2 = 0, len(right2) - 1

                        current = right1[pivot1]

                        while l2 <= r2:

                            pivot2 = l2 + (r2 - l2) // 2

                            if right2[pivot2] == current:
                                i2 = pivot2
                                break

                            elif right2[pivot2] < current:
                                l2 = pivot2 + 1
                            else:
                                r2 = pivot2 - 1

                        i2 = i2 if i2 != -1 else l2
                        # fixme fixed
                        left1, right1 = left1 + right1[:pivot1 + 1], right1[pivot1 + 1:]

                        # len_left, len_right = len(
                        #     left1) + len(left2), len(right1) + len(right2)
                        #
                        # if abs(len_left-len_right)>2:

                        left2, right2 = left2 + right2[:i2 + 1], right2[i2 + 1:]


                    else:
                        pivot2 = 0 + (len(right2) - 1 - 0) // 2

                        l1, r1 = 0, len(right1) - 1

                        current = right2[pivot2]

                        while l1 <= r1:

                            pivot2 = l1 + (r1 - l1) // 2

                            if right1[pivot1] == current:
                                i1 = pivot1
                                break

                            elif right1[pivot1] < current:
                                l1 = pivot1 + 1
                            else:
                                r1 = pivot1 - 1

                        i1 = i1 if i1 != -1 else l1
                        # fixme fixed
                        left1, right1 = left1 + right1[:i1 + 1], right1[i1 + 1:]
                        left2, right2 = left2 + right2[:pivot2 + 1], right2[pivot2 + 1:]



            else:

                if len(left2) == 0:
                    pivot1 = 0 + (len(left1) - 1 - 0) // 2

                    # fixme fixed

                    left1, right1 = left1[:pivot1 + 1], left1[pivot1 + 1:] + right1


                elif len(left1) == 0:
                    i2 = 0 + (len(left2) - 1 - 0) // 2

                    # fixme fixed
                    left2, right2 = left2[:i2 + 1], left2[i2 + 1:] + right2

                elif left1[-1] == left2[-1]:

                    right1,left1 = [left1[-1]]+right1,left1[:-1]

                else:

                    if left1[-1] > left2[-1]:
                        pivot1 = 0 + (len(left1) - 1 - 0) // 2

                        l2, r2 = 0, len(left2) - 1

                        current = left1[pivot1]

                        while l2 <= r2:

                            pivot2 = l2 + (r2 - l2) // 2

                            if left2[pivot2] == current:
                                i2 = pivot2
                                break

                            elif left2[pivot2] < current:
                                l2 = pivot2 + 1
                            else:
                                r2 = pivot2 - 1

                        i2 = i2 if i2 != -1 else l2
                        # fixme fixed
                        right1, left1 = left1[pivot1 + 1:] + right1, left1[:pivot1 + 1]
                        right2, left2 = left2[i2 + 1:] + right2, left2[:i2 + 1]




                    else:
                        pivot2 = 0 + (len(left2) - 1 - 0) // 2

                        l1, r1 = 0, len(left1) - 1

                        current = left2[pivot2]

                        while l1 <= r1:

                            pivot1 = l1 + (r1 - l1) // 2

                            if left1[pivot1] == current:
                                i1 = pivot1
                                break

                            elif left1[pivot1] < current:
                                l1 = pivot1 + 1
                            else:
                                r1 = pivot1 - 1

                        i1 = i1 if i1 != -1 else l1
                        # fixme fixed
                        right1, left1 = left1[i1 + 1:] + right1, left1[:i1 + 1],
                        right2, left2 = left2[pivot2 + 1:] + right2, left2[:pivot2 + 1]

            # print()
            # print(left1, right1)
            # print(left2, right2)
            # import time
            # time.sleep(1)
            len_left, len_right = len(
                left1) + len(left2), len(right1) + len(right2)

        # result
        if len_left == len_right:

            first = left1[-1] if len(left2) == 0 else left2[-1] if len(left1) == 0 else max(left1[-1],
                                                                                            left2[-1])
            sec = right1[0] if len(right2) == 0 else right2[0] if len(right1) == 0 else min(right1[0],
                                                                                            right2[0])

            return (first + sec) / 2

        elif len_left < len_right:

            return right1[0] if len(right2) == 0 else right2[0] if len(right1) == 0 else min(right1[0],
                                                                                             right2[0])
        else:
            return left1[-1] if len(left2) == 0 else left2[-1] if len(left1) == 0 else max(left1[-1], left2[-1])

        
# @lc code=end

