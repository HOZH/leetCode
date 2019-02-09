package algorithms;

public class q766 {


    public boolean isToeplitzMatrix(int[][] matrix) {


        int current;


        for (int i = 0; i < matrix.length; i++) {

            for (int j = 0; j < matrix[0].length; j++) {

                if (i < matrix.length - 1 && j < matrix[0].length - 1) {
                    current = matrix[i][j];

                    if (current != matrix[i + 1][j + 1])
                        return false;

                }

            }

        }


        return true;
    }
}
