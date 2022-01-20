class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:

        N = len(arr)
        
        if N==1: return arr[0]
        if N==2: return arr[0]*arr[2]

        dp = [[float('inf')]*N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if j==i:
                    dp[i][j] = 0
                    
        for i in range(N-1):
            for k in range(i, N-1):
                for j in range(k+1, N):
                    print(dp, i, k, j)
                    dp[i][j] = max(arr[i:k+1])*max(arr[k+1:j+1])+dp[i][k]+dp[k+1][j]
                    
            
            
        print(dp)
        return max(dp)



    """
        [   48    ]
        [ 12  32 ]
        [6,2,4,8]


                48
        [   24    ]
        [ 12   ]
        [6,2,4,8]
        
        
        
               48 
        24
            8
        [6,2,4,8]
        """

    def mctFromLeafValues(self, A):
        res = 0
        while len(A) > 1:
            i = A.index(min(A))
            res += min(A[i - 1:i] + A[i + 1:i + 2]) * A.pop(i)
        return res