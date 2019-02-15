package amazon;

import java.util.Arrays;

public class practiceQ1 {

    public static void main(String[] args) {

        int[] a= {1,0,0,0,0,1,0,0};
        int[] b={1,1,1,0,1,1,1,1};

//        Arrays.stream(cellCompete(a, 1)).forEach(x->System.out.print(x+" "));
        System.out.println();
        Arrays.stream(cellCompete(b, 2)).forEach(x->System.out.print(x+" "));
    }


    public static int[] cellCompete(int[] cells, int days) {
        // INSERT YOUR CODE HERE


        int[] result = Arrays.copyOf(cells, cells.length);


        for (int i = 0; i < days; i++) {
            cells = Arrays.copyOf(result, result.length);
            boolean left = false;
            boolean right = false;
            for (int j = 0; j < cells.length; j++) {
                left = false;

                right = false;

                if (j - 1 >= 0) {
                    if (cells[j - 1] == 1)
                        left = true;
                }

                if (j + 1 <= cells.length - 1) {
                    if (cells[j + 1] == 1)
                        right = true;
                }



                if (left == right) {
                    result[j] = 0;

                } else {

                    result[j] = 1;
                }




            }


        }


        return result;
    }
}
