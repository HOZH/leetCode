from collections import Counter


class Solution:
    def mostCommonWord(self, paragraph: str, banned):
        # gonna redo this question after I reviewed regular ex
        temp = paragraph.casefold().replace(',', ' ', -1).replace(';', ' ', -1).replace('\'', ' ', -1).replace('?', ' ', -1).replace('.',
                                                                                                                                     ' ', -1).replace('!', ' ', -1).split()

        temp = list(filter(lambda x: x not in banned, temp))

        c = Counter(temp)

        answer = []

        print(c.most_common())

        most = c.most_common()[0][1]

        for i in range(len(c.most_common())):

            if c.most_common()[i][1] ==most:


                answer.append(c.most_common()[i][0])

        return answer









a = Solution()


print(a.mostCommonWord("once upon upon once something",[]))
