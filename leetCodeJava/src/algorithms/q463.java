package algorithms;

public class q463 {

    public int islandPerimeter(int[][] grid) {

        int primeter = 0;

        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {

                if (grid[i][j] == 1) {
                    if (i - 1 < 0 || grid[i - 1][j] == 0)
                        primeter++;
                    if (i + 1 == grid.length || grid[i + 1][j] == 0)
                        primeter++;
                    if (j - 1 < 0 || grid[i][j - 1] == 0)
                        primeter++;
                    if (j + 1 == grid[0].length || grid[i][j + 1] == 0)
                        primeter++;
                }


            }
        }

        return primeter;
    }
}
