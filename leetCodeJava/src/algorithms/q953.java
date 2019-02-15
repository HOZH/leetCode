package algorithms;

public class q953 {

    public boolean isAlienSorted(String[] words, String order) {


        for (int i = 0; i < words.length - 1; i++) {

            if (!checker(words[i], words[i + 1], order))

                return false;

        }


        return true;
    }


    int charValue(char ch, String order) {

        int value = 0;
        char[] chars = order.toCharArray();
        for (int i = 0; i < chars.length; i++) {
            if (ch == chars[i]) {
                value = i;
                break;
            }
        }
        return value;
    }


    boolean checker(String word1, String word2, String order) {
        char[] chars = order.toCharArray();
        int a;
        int b;

        for (int i = 0; i < word1.toCharArray().length; i++) {

            if (i < word1.length()) {
                a = charValue(word1.charAt(i), order);
            } else {
                a = 0;
            }

            if (i < word2.length()) {
                b = charValue(word2.charAt(i), order);
            } else {
                b = 0;
            }

            if (a == b) {
                continue;
            } else if (a > b) {


                return false;
            } else if (a < b)
                return true;

        }


        return true;

    }

}
