package algorithms;

import java.util.Arrays;

public class q908 {

    public int smallestRangeI(int[] A, int K) {


        Arrays.sort(A);

        int min =A[0];
        int max=A[A.length-1];

        if(2*K>=Math.abs(max-min)){

            return 0;
        }

        else return Math.abs(max-min)-2*K;
    }

}
