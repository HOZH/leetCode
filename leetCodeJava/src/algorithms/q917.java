package algorithms;

public class q917 {

    public String reverseOnlyLetters(String S) {

        int key = 0;
        int pureStringIndex = 0;

        char[] resultArr = new char[S.length()];
        for (int i = 0; i < S.length(); i++) {
            if (!Character.isAlphabetic(S.charAt(i))) {
                resultArr[i] = S.charAt(i);
                key++;

            }
        }
        char[] pureString = new char[S.length() - key];

        for (int i = 0; i < S.length(); i++) {
            if (Character.isAlphabetic(S.charAt(i))) {
                pureString[pureStringIndex++] = S.charAt(i);
            }

        }

        int count = 0;
        for (int i = resultArr.length - 1; i >= 0; i--) {
            if (resultArr[i] == 0) {
                resultArr[i] = pureString[count++];
            }

        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < resultArr.length; i++) {
            sb.append(resultArr[i]);
        }

        return sb.toString();
    }
}
