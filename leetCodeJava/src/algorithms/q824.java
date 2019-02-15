package algorithms;

public class q824 {

    public String toGoatLatin(String S) {


        String str;


        String[] strs = S.split(" ");
        String temp;

        for (int i = 0; i < strs.length; i++) {


            if (strs[i].charAt(0) == 'a' || strs[i].charAt(0) == 'e' || strs[i].charAt(0) == 'i' || strs[i].charAt(0) == 'o' || strs[i].charAt(0) == 'u' || strs[i].charAt(0) == 'A' || strs[i].charAt(0) == 'E' || strs[i].charAt(0) == 'I' || strs[i].charAt(0) == 'O' || strs[i].charAt(0) == 'U') {
                strs[i] = strs[i] + "ma";

            } else {

                temp = strs[i];
                strs[i] = strs[i].substring(1) + temp.charAt(0) + "ma";

            }

            for (int j = 0; j < i + 1; j++) {
                strs[i] += "a";
            }


        }

        str = String.join(" ", strs);


        return str;
    }


}
