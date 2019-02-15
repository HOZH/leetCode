package algorithms;

import java.util.Arrays;

public class q976 {

    public int largestPerimeter(int[] A) {

        Arrays.sort(A);

        int a;
        int b;
        int c;
        int temp = A.length - 1;


        a = A[temp];
        b = A[temp - 1];
        c = A[temp - 2];


        while (b + c <= a) {
            if (temp - 3 < 0) {
                return 0;
            }
            a = A[--temp];
            b = A[temp - 1];
            c = A[temp - 2];


        }


        return a + b + c;
    }


}
