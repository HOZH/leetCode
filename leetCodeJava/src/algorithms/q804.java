package algorithms;

import java.util.HashSet;

public class q804 {

    public static final String[] morseCode = {".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."};

    public static void main(String[] args) {

        String[] words = {"gin", "zen", "gig", "msg"};

        System.out.println(uniqueMorseRepresentations(words));


    }

    public static int uniqueMorseRepresentations(String[] words) {

        var resultStrs = new String[words.length];

        for (int i = 0; i < words.length; i++) {
            char[] chars = words[i].toCharArray();
            StringBuilder resultStr = new StringBuilder();
            for (char c : chars) {
                int char2Ascii = (int) c;

                var currentStr = morseCode[char2Ascii - 97];
                resultStr.append(currentStr);
            }
            resultStrs[i] = resultStr.toString();
        }

        HashSet<String> hashSet = new HashSet<>();
        for (String s : resultStrs)
            hashSet.add(s);
        return hashSet.size();

    }
}
