package algorithms;


public class q771 {
    public static void main(String[] args) {


        System.out.println(numJewelsInStones("z", "ZZ"));


    }

    public static int numJewelsInStones(String J, String S) {

        char[] js = J.toCharArray();
        char[] ss = S.toCharArray();

        int count = 0;
        for (char j : js) {

            for (char s : ss) {
                if (j == s) {
                    count++;

                }
            }

        }


        return count;
    }
}
