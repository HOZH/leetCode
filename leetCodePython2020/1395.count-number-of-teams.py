#
# @lc app=leetcode id=1395 lang=python3
#
# [1395] Count Number of Teams
#

# @lc code=start


class Solution:

    def helper(self, lis, l, index):
        first = lis[0]
        local_count = 0
        if l == 2:
            if index in self.memo:
                return self.memo[index]

        for i in range(1, len(lis)):

            if first < lis[i]:
                if l == 2:
                    local_count += 1
                else:
                    next_index = index+1+i
                    if next_index in self.memo:
                        local_count += self.memo[next_index]

                    else:
                        local_count += self.helper(
                            lis[i:], l - 1, next_index)

        if l == 2:
            self.memo[index] = local_count
        return local_count

    def numTeams(self, rating) -> int:

        result = 0
        rev = rating[::-1]
        length = len(rating)

        self.memo = dict()

        for i in range(length-3, -1, -1):
            current = rating[i:]
            result += self.helper(current, 3, 0+i)

        self.memo = dict()

        for i in range(length-3, -1, -1):
            current = rev[i:]
            result += self.helper(current, 3, 0+i)

        return result
