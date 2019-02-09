package algorithms;

import java.util.ArrayList;

public class q500 {

    public String[] findWords(String[] words) {

        String first = "qwertyuiop";
        String sec = "asdfghjkl";
        String third = "zxcvbnm";

//        String[] strs = {first, sec, third};

        boolean qualified = true;

        ArrayList<String> resultList = new ArrayList<String>();
        for (int j =0;j<words.length;j++) {
            String s=words[j];
            if (first.contains(String.valueOf(s.charAt(0)).toLowerCase())) {
                for (int i = 1; i < s.length(); i++) {
                    if (!first.contains(String.valueOf(s.charAt(i)).toLowerCase())) {
                        qualified = false;
                        break;
                    }
                }

            } else if (sec.contains(String.valueOf(s.charAt(0)).toLowerCase())) {
                for (int i = 1; i < s.length(); i++) {
                    if (!sec.contains(String.valueOf(s.charAt(i)).toLowerCase())) {
                        qualified = false;
                        break;
                    }
                }

            } else if (third.contains(String.valueOf(s.charAt(0)).toLowerCase())) {
                for (int i = 1; i < s.length(); i++) {
                    if (!third.contains(String.valueOf(s.charAt(i)).toLowerCase())) {
                        qualified = false;
                        break;
                    }
                }

            }

            if(qualified!=false)
                resultList.add(s);

            qualified=true;

        }

        return resultList.stream().toArray(String[]::new);


    }
}
