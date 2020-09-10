#
# @lc app=leetcode id=1105 lang=python3
#
# [1105] Filling Bookcase Shelves
#

# @lc code=start


class Solution:
    def minHeightShelves_wrong_since_only_consider_the_prev_1_book(self, books, shelf_width: int) -> int:
        len_books = len(books)
        if not len_books:
            return 0
        dp = [[[] for _ in range(2)] for _ in range(len_books)]
        # dp [ith][new layer] = current_height,remain_width,total_height
        # thickness books[i][0] and height books[i][1].
        inf = float('inf')
        dp[0][0] = 1001, -1, inf
        dp[0][1] = books[0][1], shelf_width-books[0][0], books[0][1]

        for i in range(1, len_books):
            # no enough width for appending book into current layer
            if dp[i-1][0][1] < books[i][0] and dp[i-1][1][1] < books[i][0]:
                dp[i][0] = (inf, -1, inf)
            else:
                on_prev_append = (inf, -1, inf) if dp[i-1][0][1] < books[i][0] else (max(books[i][1], dp[i-1][0][0]),
                                                                                     dp[i-1][0][1]-books[i][0], dp[i-1][0][2]-dp[i-1][0][0]+max(books[i][1], dp[i-1][0][0]))
                on_prev_new = (inf, -1, inf) if dp[i-1][1][1] < books[i][0] else (max(books[i][1], dp[i-1][1][0]),
                                                                                  dp[i-1][1][1]-books[i][0], dp[i-1][1][2]-dp[i-1][1][0]+max(books[i][1], dp[i-1][1][0]))
                dp[i][0] = min(on_prev_append, on_prev_new, key=lambda x: x[2])
            dp[i][1] = books[i][1], shelf_width - \
                books[i][0], min(dp[i-1][0][2], dp[i-1][1][2])+books[i][1]
        return min(dp[-1][0][2], dp[-1][1][2])

    def minHeightShelves(self, books, shelf_width: int) -> int:
        dp = [1000**2+1]*len(books)
        for j in range(len(books)):
            max_h, current_width = 0, 0

            for i in range(j, -1, -1):

                current_width += books[i][0]

                if current_width > shelf_width:
                    break

                max_h = max(max_h, books[i][1])
                dp[j] = min(dp[j], (0 if i == 0 else dp[i-1])+max_h)

        return dp[-1]

    # Note again that at each step of the above process, the order of the books we place is the same order as the given sequence of books.  For example, if we have an ordered list of 5 books, we might place the first and second book onto the first shelf, the third book on the second shelf, and the fourth and fifth book on the last shelf.

    def minHeightShelves_wrong(self, books, shelf_width: int) -> int:
        # total height, height limit, remaining shelf space
        dp = [[[0, 0, 0], [0, 0, 0]] for _ in range(len(books))]

        # dp[i][0] = use remaining space of current layer, if not enough space left, the value is same as [i][1]
        # dp[i][1] = skip to next layer

        dp[0] = [[0, books[0][1], shelf_width-books[0][0]],
                 [0, books[0][1], shelf_width-books[0][0]]]

        for i in range(1, len(books)):
            prev = dp[i-1][0]
            enough_w = prev[2]-books[i][0] >= 0
            if enough_w:
                temp_01 = [prev[0], max(
                    prev[1], books[i][1]), prev[2]-books[i][0]]
            else:
                temp_01 = [prev[0]+prev[1], books[i]
                           [1], shelf_width-books[i][0]]

            temp_02 = [prev[0]+prev[1], books[i][1], shelf_width-books[i][0]]

            prev = dp[i-1][1]
            enough_w = prev[2]-books[i][0] >= 0
            if enough_w:
                temp_11 = [prev[0], max(
                    prev[1], books[i][1]), prev[2]-books[i][0]]
            else:
                temp_11 = [prev[0]+prev[1], books[i]
                           [1], shelf_width-books[i][0]]

            temp_12 = [prev[0]+prev[1], books[i][1], shelf_width-books[i][0]]

            if temp_01[0] > temp_11[0]:
                dp[i] = [temp_11, temp_12]
            else:
                dp[i] = [temp_01, temp_02]
        print(dp)
        temp = dp[-1]
        a = temp[0][0]+temp[0][1]
        b = temp[1][0]+temp[1][1]
        return min(a, b)
        # return dp[-1][0]+dp[-1][1]

    def minHeightShelves_best_fit(self, books: List[List[int]], shelf_width: int) -> int:
        if len(books) == 0:
            return 0
        # for i in books:
        #     if i[0] > shelf_width:
        #         return 0

        books.sort(key=lambda x: x[1])
        print(books)

        def helper(remain_book, remain_w, height):
            # height = 0 means no book has been added to current layer of shelf

            current = None
            current_index = None

            # find a book that can fit into remainning width
            for i in range(len(remain_book)-1, -1, -1):
                if remain_book[i][0] <= remain_w:
                    current = remain_book[i]
                    current_index = i
                    break
            # if not found, go to next layer
            if current is None:
                if height == 0:
                    return 0
                return height+helper(remain_book, shelf_width, remain_book[-1][1])

            else:
                #
                remain_book = remain_book[:current_index] + \
                    remain_book[current_index+1:]

                if len(remain_book) == 0:
                    return height
                if remain_w - current[0] == 0:
                    return height + helper(remain_book, shelf_width, remain_book[-1][1])
                else:
                    return helper(remain_book, remain_w - current[0], height)

        return helper(books, shelf_width, books[-1][1])


# @lc code=end
