#
# @lc app=leetcode id=1329 lang=python3
#
# [1329] Sort the Matrix Diagonally
#

# @lc code=start


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:

        flat_list, dias = [], []
        m, n = len(mat), len(mat[0])
        result = [[0]*n for i in range(m)]

        for i in range(n-1, -1, -1):
            temp = i
            j = 0
            dia = []

            while j < m and temp < n:
                if temp == n:
                    break
                dia.append(mat[j][temp])
                temp += 1
                j += 1

            dia.sort()
            dias.insert(0, dia)

        for i in range(1, m):

            temp = 0
            temp_i = i
            dia = []
            while temp_i < m and temp < n:

                dia.append(mat[temp_i][temp])
                temp += 1
                temp_i += 1

            dia.sort()
            dias.insert(0, dia)

        for i in dias:
            flat_list.extend(i)

        current_index = 0

        for i in range(m-1, -1, -1):
            temp_i = i
            temp_j = 0

            while temp_i < m and temp_j < n:
                result[temp_i][temp_j] = flat_list[current_index]
                current_index += 1
                temp_i += 1
                temp_j += 1

        for j in range(1, n):
            temp_i = 0
            temp_j = j

            while temp_i < m and temp_j < n:
                result[temp_i][temp_j] = flat_list[current_index]
                current_index += 1
                temp_i += 1
                temp_j += 1

        return result


# @lc code=end
