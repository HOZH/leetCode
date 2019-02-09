package algorithms;


import java.util.ArrayList;
import java.util.HashMap;

public class q884 {

    public String[] uncommonFromSentences(String A, String B) {

        String[] strs1 = A.split(" ");
        String[] strs2 = B.split(" ");


        HashMap<String, Integer> resultMap = new HashMap<>();

        for (String s : strs1) {
            if (resultMap.get(s) != null)
                resultMap.put(s, resultMap.get(s) + 1);
            else
                resultMap.put(s, 1);

        }
        for (String s : strs2) {
            if (resultMap.get(s) != null)
                resultMap.put(s, resultMap.get(s) + 1);
            else
                resultMap.put(s, 1);

        }

        ArrayList<String> resultList = new ArrayList<>();

        for (String s : resultMap.keySet()) {
            if (resultMap.get(s) == 1) {
                resultList.add(s);
            }
        }

        return resultList.stream().toArray(String[]::new);
    }
}
