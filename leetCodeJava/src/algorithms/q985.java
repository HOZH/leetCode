package algorithms;

import java.util.Arrays;
import java.util.OptionalInt;

public class q985 {

    public int[] sumEvenAfterQueries(int[] A, int[][] queries) {


        int[] tempArr = new int[A.length];

        for (int i = 0; i < queries.length; i++) {

            A[queries[i][1]] += queries[i][0];


            OptionalInt temp = Arrays.stream(A).filter(x -> x % 2 == 0).reduce((a, b) -> (a + b));

            if (temp.isPresent())
                tempArr[i] = temp.getAsInt();



        }

        return tempArr;
    }
}