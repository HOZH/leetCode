package algorithms;

import java.util.Arrays;

public class q922 {


    public int[] sortArrayByParityII(int[] A) {


        int[] odds = Arrays.stream(A).filter(x -> x % 2 != 0).toArray();

        int[] evens = Arrays.stream(A).filter(x -> x % 2 == 0).toArray();


        int[] result = new int[A.length];

        int currentOdd = 0;
        int currentEven = 0;

        for (int i = 0; i < A.length; i++) {

            if (i % 2 == 0) {

                result[i] = evens[currentEven++];

            } else result[i] = odds[currentOdd++];
        }


        return result;
    }
}
