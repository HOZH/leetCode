package algorithms;


public class q461 {

    public static void main(String[] args) {

        System.out.println(hammingDistance(15, 2));
    }


    public static int hammingDistance(int x, int y) {

        int count = 0;

        int xor = x ^ y;

        String xorInBinary = Integer.toBinaryString(xor);

        System.out.println(xorInBinary);

        for (char c : xorInBinary.toCharArray()) {
            if (c == '1') count++;
        }


        return count;

    }


}
