
class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        numbers = []
        numberStrs = []
        results = []
        for i in range(left, right + 1):

            a = [l for l in str(i) if not (l == '0')]

            if(len(a) == len(str(i))):

                numbers.append(i)
        for i in range(len(numbers)):
            tempList = []
            for s in str(numbers[i]):
                tempList.append(s)
            numberStrs.append(tempList)

        isSelfDividing = bool()
        isSelfDividing = True
        for i in range(len(numbers)):

            for j in range(len(numberStrs[i])):

                num = int(numberStrs[i][j])
                if(numbers[i] % num):
                    isSelfDividing = False

                    break
            if(isSelfDividing):
                results.append(numbers[i])
            else:
                isSelfDividing = True
        return results


so = Solution()
so.selfDividingNumbers(1, 22)
