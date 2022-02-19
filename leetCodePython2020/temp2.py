from functools import lru_cache
class Solution:
    def countArrangement(self, n: int) -> int:
        return len(genArrangements(n))
    
    
def genArrangements(n):
    if n==1:
        return [[1]]
    
    newArrangements = [arrangement+[n] for arrangement in genArrangements(n-1)]
    divisibleArrangements = []
    for arrangement in newArrangements:
        for i in range(n-1):
            if isDivisible(arrangement[-1], i+1) and isDivisible(arrangement[i], n):
                toSwapArrangement = arrangement[:]
                toSwapArrangement[i], toSwapArrangement[-1] = toSwapArrangement[-1], toSwapArrangement[i]
                divisibleArrangements.append(toSwapArrangement)
    print(n, newArrangements, divisibleArrangements)
    return newArrangements + divisibleArrangements
    
def isDivisible(n, i):
    if i==0 or n==0:
        return False
    return n%i==0 or i%n==0

"""
2 [[1, 2]] [[2, 1]]
3 [[1, 2, 3], [2, 1, 3]] [[3, 2, 1]]
4 [[1, 2, 3, 4], [2, 1, 3, 4], [3, 2, 1, 4]] [[4, 2, 3, 1], [1, 4, 3, 2], [4, 1, 3, 2], [2, 4, 3, 1], [3, 4, 1, 2]]
5 [[1, 2, 3, 4, 5], [2, 1, 3, 4, 5], [3, 2, 1, 4, 5], [4, 2, 3, 1, 5], [1, 4, 3, 2, 5], [4, 1, 3, 2, 5], [2, 4, 3, 1, 5], [3, 4, 1, 2, 5]] [[5, 2, 3, 4, 1], [5, 4, 3, 2, 1]]
6 [[1, 2, 3, 4, 5, 6], [2, 1, 3, 4, 5, 6], [3, 2, 1, 4, 5, 6], [4, 2, 3, 1, 5, 6], [1, 4, 3, 2, 5, 6], [4, 1, 3, 2, 5, 6], [2, 4, 3, 1, 5, 6], [3, 4, 1, 2, 5, 6], [5, 2, 3, 4, 1, 6], [5, 4, 3, 2, 1, 6]] 

[[6, 2, 3, 4, 5, 1], [1, 6, 3, 4, 5, 2], [1, 2, 6, 4, 5, 3], [6, 1, 3, 4, 5, 2], [2, 6, 3, 4, 5, 1], [2, 1, 6, 4, 5, 3], [6, 2, 1, 4, 5, 3], [3, 6, 1, 4, 5, 2], [3, 2, 6, 4, 5, 1], [4, 6, 3, 1, 5, 2], [4, 2, 6, 1, 5, 3], [6, 4, 3, 2, 5, 1], [1, 4, 6, 2, 5, 3], [4, 6, 3, 2, 5, 1], [4, 1, 6, 2, 5, 3], [6, 4, 3, 1, 5, 2], [2, 4, 6, 1, 5, 3], [6, 4, 1, 2, 5, 3], [3, 4, 6, 2, 5, 1], [5, 6, 3, 4, 1, 2], [5, 2, 6, 4, 1, 3], [5, 4, 6, 2, 1, 3]]


"""


class Solution:
    def countArrangement(self, n: int) -> int:

        self.lis = set([i for i in range(1, n + 1)])
        self.ans = set()

        @lru_cache(None)
        def helper(temp_lis):
            if temp_lis.count(0) == 1:
                self.ans.add(temp_lis)
                return
            for i in range(1, n + 1):
                if temp_lis[i] == 0:
                    for chosen in list(self.lis):
                        if i % chosen == 0 or chosen % i == 0:
                            new_temp_lis = list(temp_lis[:])
                            new_temp_lis[i] = chosen
                            self.lis.remove(chosen)
                            helper(tuple(new_temp_lis))
                            self.lis.add(chosen)
                    break
        helper(tuple([0 for _ in range(n + 1)]))

        return len(self.ans)



class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        M, N = len(nums1), len(nums2)
        memo = [[0]*(N+1) for _ in range(M+1)]
        for i in range(1, M+1):
            for j in range(1, N+1):
                if nums1[i-1]==nums2[j-1]:
                    memo[i][j] = memo[i-1][j-1]+1
                else:
                    memo[i][j] = max(memo[i-1][j], memo[i][j-1])
        return memo[-1][-1]


class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:

        n = len(A)
        m = len(B)

        # Edge cases.
        if m == 0 or n == 0:
            return 0

        if n == 1 and m == 1:
            if A[0] == B[0]:
                return 1
            else:
                return 0

        # Initializing first row and column with 0 (for ease i intialized everthing 0 :p)
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        # this code is a lot like longest common subsequence(only else condition is different).
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                # else:
                #     dp[i][j] = 0

        return max([item for sublist in dp for item in sublist])
