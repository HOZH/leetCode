package algorithms;

public class q896 {
    public boolean isMonotonic(int[] A) {


        if (A.length > 2) {
            int inc = 2;

            for (int i = 0; i < A.length - 1; i++) {

                if (A[i] > A[i + 1]) {

                    if (inc == 1)
                        return false;

                    inc = 0;
                } else if (A[i] < A[i + 1]) {

                    if (inc == 0)
                        return false;

                    inc = 1;
                }


            }


        }

        return true;

    }
}
