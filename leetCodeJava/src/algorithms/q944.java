package algorithms;

import java.util.Arrays;

public class q944 {

    public int minDeletionSize(String[] A) {

        int size = A.length;

        int strSize = A[0].length();

        int deletionCount = 0;

        String temp;
        char[] sorted;
        for (int i = 0; i < strSize; i++) {

            temp = "";

            for (int j = 0; j < size; j++) {

                temp += A[j].charAt(i);

            }


            sorted = temp.toCharArray();
            Arrays.sort(sorted);
            if (!temp.equals(new String(sorted))) {

                deletionCount++;


            }


        }


        return deletionCount;
    }
}
