package algorithms;

import java.util.Arrays;

public class q905 {

    public int[] sortArrayByParity(int[] A) {

        int[] evens = Arrays.stream(A).filter(x -> (x % 2 != 0)).toArray();

        int[] odds = Arrays.stream(A).filter(x -> (x % 2 == 0)).toArray();


        int[] result = new int[A.length];

        System.arraycopy(odds, 0, result, 0, odds.length);
        System.arraycopy(evens, 0, result, odds.length, evens.length);


        return result;

    }
}
