class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        maxFlowers = 0
        
        if flowerbed[0]==0 and len(flowerbed)==1 or flowerbed[0]==0 and flowerbed[1]==0:
            flowerbed[0]=1
            maxFlowers+=1
        if flowerbed[-1]==0 and len(flowerbed)==1 or flowerbed[-1]==0 and flowerbed[-2]==0:
            flowerbed[-1]=1
            maxFlowers+=1
        
        
        for i in range(len(flowerbed)):
            if 1<=i<len(flowerbed)-1 and flowerbed[i-1]==0 and flowerbed[i]==0 and flowerbed[i+1]==0:
                flowerbed[i]=1
                maxFlowers+=1

        return n<=maxFlowers


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True

        current_index, prev_index, next_index = 0, -1, 1

        while next_index <= len(flowerbed):

            if flowerbed[current_index] != 1:
                if (prev_index < 0 or flowerbed[prev_index] == 0) and (next_index == len(flowerbed) or flowerbed[next_index] == 0):
                    flowerbed[current_index] = 1
                    n -= 1
                    if (n == 0):
                        return True
            prev_index = current_index
            current_index = next_index
            next_index += 1
        return False
