#
# @lc app=leetcode id=698 lang=python3
#
# [698] Partition to K Equal Sum Subsets
#

# @lc code=start


from collections import Counter


class Solution:
    def canPartitionKSubsets(self, nums, k):
        total = sum(nums)
        if total % k != 0:
            return False

        self.partial_sum = total//k
        nums = sorted(nums)

        if nums[-1] > self.partial_sum:
            return False

        def recurse(index, subsets):
            if index < 0:
                return True
            tried = set()

            for i in range(len(subsets)):
                if subsets[i] in tried:
                    continue
                if subsets[i]+nums[index] <= self.partial_sum:
                    subsets[i] += nums[index]

                    if recurse(index-1, subsets):
                        return True

                    subsets[i] -= nums[index]

                tried.add(subsets[i])

            return False

        return recurse(len(nums)-1, [0]*k)

    def canPartitionKSubsets_1(self, nums, k: int) -> bool:

        self.record = dict()

        for i in range(0, k + 1):
            self.record[i] = []

        if sum(nums) % k != 0:
            return False

        partial_sum = sum(nums) // k

        # nums.sort()

        def helper(n, current, target, k):
            # if len(n) == 0:
            #     return False
            if len(n) < k:
                return False
            # if n[-1] > target:
            #     return False
            if max(n) > target:
                return False
            if current == target:
                if sum(n) != target * k:
                    return False

                # counts = dict()
                # for j in n:
                #     if j not in counts:
                #         counts[j] = 1
                #     else:
                #         counts[j] += 1
                counts = Counter(n)

                if counts not in self.record[k]:
                    self.record[k].append(counts)
                else:
                    return False

            used = set()
            for i in range(len(n)):

                temp = n[i]
                # if temp > current:
                #     continue
                if temp not in used:

                    used.add(temp)

                    remaining = current - temp

                    if remaining < 0:
                        return False
                    elif remaining == 0:
                        if k == 1:
                            return True
                        # counts = dict()
                        # for j in n[:i] + n[i + 1:]:
                        #     if j not in counts:
                        #         counts[j] = 1
                        #     else:
                        #         counts[j] += 1
                        #
                        # if counts not in self.record[k - 1]:
                        #     self.record[k-1].append(counts)
                        # if 1==1:

                        if helper(n[:i] + n[i + 1:], target, target, k - 1):
                            return True

                        # else:
                        #     # print('in')
                        #     # print(counts,k-1,self.record[k-1])
                        #     pass

                    # elif remaining < 0:
                    #     return False
                    else:
                        if helper(n[:i] + n[i + 1:], remaining, target, k):
                            return True
            return False

        return helper(nums, partial_sum, partial_sum, k)

# @lc code=end
