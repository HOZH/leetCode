class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        M, N = len(mat), len(mat[0])
        hash_dict = {}
        for i in range(M):
            for j in range(N):
                if mat[i][j] not in hash_dict:
                    hash_dict[mat[i][j]]=0
                hash_dict[mat[i][j]]+=1
        print(hash_dict)
        return max(hash_dict.values())==M

class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        sets = []
        for row in mat:
            sets.append(set(row))
        temp = list(reduce(lambda x, y: x & y, sets))
        if not len(temp):
            return -1
        return min(temp)

m * n 
"""
m*n

1111
1 1 225
1133


n*m*log(n)
 log(m)


nm log(n)nm lo"""


 n*m

 

