package amazon;

import java.util.Arrays;

public class practiceQ2 {

    public static void main(String[] args) {


    }


    public static int generalizedGCD(int arr[]) {
        // INSERT YOUR CODE HERE

        Arrays.sort(arr);
        int gcd = 1;
        boolean isCd = true;

        for (int i = 2; i <= arr[0]; i++) {


            for (int j : arr) {
                if (j % i != 0) {
                    isCd = false;
                    break;
                }

            }

            if (isCd) {
                gcd = i;
            } else isCd = true;

        }


        return gcd;
    }
}