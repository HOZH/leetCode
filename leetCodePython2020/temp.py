

from collections import deque
from itertools import permutations
test = [10, 4, -8, 7]


def foo(arr):

    left_sum, right_sum = sum(arr), 0

    count = 0

    for i in range(len(arr)-1, 0, -1):

        temp = arr[i]

        left_sum -= temp
        right_sum += temp

        count += 0 if left_sum <= right_sum else 1

    return count


print(foo(test))


a = "GeEK"

# no length entered so default length
# taken as 4(the length of string GeEK)
p = permutations(a)

# Print the obtained permutations
for j in set(p):
    print(j)


# Demolition Robot
# Given a matrix with values 0 (trenches), 1 (flat), and 9 (obstacle) you have to find minimum distance to reach 9 (obstacle). If not possible then return -1.
# The demolition robot must start at the top left corner of the matrix, which is always flat, and can move on block up, down, right, left.
# The demolition robot cannot enter 0 trenches and cannot leave the matrix.
# Sample Input:
# [1, 0, 0],
# [1, 0, 0],
# [1, 9, 1]]
#     Sample Output:
#     3
#     This question can be solved by using BFS or DFS.


def bar(matrix):

    row_len, col_len = len(matrix), len(matrix[0])
    if not matrix[0][0]:
        return -1
    if matrix[0][0] == 9:
        return 0

    visited = set()

    positions = ((0, -1), (0, 1), (1, 0), (-1, 0))
    queue = deque([(0, 0)])
    step = 0

    while queue:

        layer_len = len(queue)

        while layer_len:

            step += 1

            layer_len -= 1

            current_x, current_y = queue.pop()

            visited.add((current_x, current_y))

            for x, y in positions:

                temp_x = current_x+x
                temp_y = current_y+y

                if 0 <= temp_x < col_len and 0 <= temp_y < row_len:

                    if (temp_x, temp_y) not in visited:

                        if matrix[temp_x][temp_y] == 1:
                            queue.appendleft((temp_x, temp_y))

                        if matrix[temp_x][temp_y] == 9:
                            print(temp_x, temp_y)
                            return step

    return -1


a = [[1, 0, 0],
     [1, 0, 0],
     [1, 1, 9]]

print(bar(a))


def in_flight_media(duration, movies):

    movies = sorted(list(enumerate(movies)), key=lambda x: x[1])
    left, right = 0, len(movies)-1

    duration = duration-30

    current_max = 0

    result = []

    while left < right:
        current_value = movies[left][1]+movies[right][1]
        if current_value <= duration:
            if current_value == current_max:
                result.append([left, right])
            elif current_value > current_max:

                result = [[left, right]]
                current_max = current_value

            left += 1
        else:
            right -= 1
    print(result)


in_flight_media(90, [1, 10, 25, 35, 50, 60])
