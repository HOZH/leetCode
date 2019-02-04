package algorithms;

public class q942 {

    public int[] diStringMatch(String S) {


        int n = S.length();

        int[] intArr = new int[n + 1];
        int[] result = new int[n + 1];

        for (int i = 0; i <= n; i++)
            intArr[i] = i;

        int right = n;
        int left = 0;

        for (int i = 0; i < n; i++) {

            if (S.charAt(i) == 'D') {

                result[i] = intArr[right--];
                result[i + 1] = intArr[right];


            }
            if (S.charAt(i) == 'I') {

                result[i] = intArr[left++];
                result[i + 1] = intArr[left];


            }


        }


        return result;
    }

}
