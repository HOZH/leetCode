package algorithms;

import java.util.Arrays;

public class q832 {

    public static void main(String[] args) {

        int[][] ints = {{1, 1, 0}, {1, 0, 1},{0,0,0}};
        flipAndInvertImage(ints);
        System.out.println(Arrays.toString(ints[0]));
        System.out.println(Arrays.toString(ints[1]));
        System.out.println(Arrays.toString(ints[2]));

    }

    public static int[][] flipAndInvertImage(int[][] A) {

        for (int i = 0; i < A.length; i++) {
            for (int j = 0; j < A[i].length / 2; j++) {
                var temp = A[i][j];

                A[i][j] = A[i][A[i].length - 1 - j];
                A[i][A[i].length - 1 - j] = temp;
            }

            for (int j = 0; j < A[i].length; j++) {
                if (A[i][j] == 0)
                    A[i][j] = 1;
                else A[i][j] = 0;

            }


        }
        return A;
    }
}
