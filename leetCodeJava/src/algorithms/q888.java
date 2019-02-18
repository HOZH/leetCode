package algorithms;

public class q888 {

    public int[] fairCandySwap(int[] A, int[] B) {


        int[] result = {0, 0};
        int a;
        int b;

//        int aSum=Arrays.stream(A).reduce((x, y) -> x + y).getAsInt();
//        int bSum=Arrays.stream(B).reduce((x, y) -> x + y).getAsInt();

        int aSum = 0;
        int bSum = 0;

        int aLen = A.length;
        int bLen = B.length;

        for (int i = 0; i < (aLen < bLen ? bLen : aLen); i++) {

            if (i < aLen)
                aSum += A[i];
            if (i < bLen)
                bSum += B[i];
        }


        for (int i = 0; i < A.length; i++) {

            a = A[i];
            for (int j = 0; j < B.length; j++) {


                b = B[j];


                if (aSum - a + b == bSum - b + a) {
                    result[0] = a;
                    result[1] = b;
                    return result;
                }


            }
        }

        return result;
    }
}
