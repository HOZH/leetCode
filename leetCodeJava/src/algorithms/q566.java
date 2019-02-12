package algorithms;

import java.util.ArrayList;
import java.util.List;

public class q566 {

    public int[][] matrixReshape(int[][] nums, int r, int c) {

        if (nums.length*nums[0].length == r * c) {
            List<Integer> dataflow = new ArrayList<>();
            for (int i = 0; i < nums.length; i++) {
                for (int j = 0; j < nums[0].length; j++) {
                    dataflow.add(nums[i][j]);
                }
            }

            int[][] result = new int[r][c];
            int[] currentRow = new int[c];

            for (int i = 0; i < r; i++) {
                for (int j = 0; j < c; j++) {
                    currentRow[j] = dataflow.get(i * c + j);
                }
                result[i] = currentRow;
                currentRow = new int[c];
            }


            return result;

        }
        return nums;
    }
}
