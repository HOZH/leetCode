package algorithms;

import java.util.Arrays;

public class q557 {

    public String reverseWords(String s) {


        String[] strs = s.split(" ");


        strs = Arrays.stream(strs).map(x -> {

                    String tempStr = x;

                    char[] tempArr = tempStr.toCharArray();
                    char[] resultArr = new char[tempArr.length];

                    for (int i = 0; i < tempArr.length; i++) {

                        resultArr[tempArr.length - 1 - i] = tempArr[i];

                    }


                    return String.valueOf(resultArr);
                }


        ).toArray(String[]::new);

        String result = "";

        for (String str : strs) {

            result += str + " ";
        }
        return result.trim();
    }
}
