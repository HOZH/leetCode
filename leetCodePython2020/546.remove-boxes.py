#
# @lc app=leetcode id=546 lang=python3
#
# [546] Remove Boxes
#

# @lc code=start


class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:

        @functools.lru_cache(None)
        def dp(l, r, k):
            # k => how many boxes after r has same value as boxes[r]

            if l > r:
                return 0

            while l < r:
                if boxes[r-1] == boxes[r]:
                    r -= 1
                    k += 1
                else:
                    break
            # case 1
            res = dp(l, r-1, 0)+(k+1)**2

            # case 2
            last_ele = boxes[r]
            for i in range(l, r):

                if boxes[i] == last_ele:
                    if last_ele != (float('inf') if (i+1) >= r else boxes[i+1]):
                        res = max(res, dp(
                            l, i, k+1)+dp(i+1, r-1, 0))

            return res

        return dp(0, len(boxes)-1, 0)

    def removeBoxes_without_cache(self, boxes: List[int]) -> int:

        n = len(boxes)
        memo = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(n)]

        def dp(l, r, k):
            # k => how many boxes after r has same value as boxes[r]

            if l > r:
                return 0

            while l < r:
                if boxes[r-1] == boxes[r]:
                    r -= 1
                    k += 1
                else:
                    break

            if memo[l][r][k] > 0:
                return memo[l][r][k]

            # case1 base case
            # when k=0 we remove boxes[r] to get 1 points
            memo[l][r][k] = dp(l, r-1, 0)+(k+1)**2

            # case 2

            last_ele = boxes[r]
            for i in range(l, r):

                if boxes[i] == last_ele:

                    # if last_ele != (float('inf') if (i+1) >= r else boxes[i+1]):
                    # in dp(l,i,k-1), boxes[i] == boxes[r] is already ensured by condition
                    # r-1 since we add the count of last element into i's count=>(k+1)
                    # boxes r-1 is not needed to have same value as boxes r
                    # even if they are the same, the sum is diff => 2,2 => 1*1 + 1*1 instead of 2*2
                    memo[l][r][k] = max(memo[l][r][k], dp(
                        l, i, k+1)+dp(i+1, r-1, 0))

            return memo[l][r][k]

        return dp(0, n-1, 0)


# @lc code=end
