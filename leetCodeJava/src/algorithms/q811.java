package algorithms;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;

public class q811 {

    public List<String> subdomainVisits(String[] cpdomains) {


        List<String> tempList = new ArrayList<String>();
        int count = 0;
        String[] strs;
        String tempStr = "";

        for (String current : cpdomains) {

            strs = current.split(" ");
            count = Integer.valueOf(strs[0]);
            tempStr = strs[1];

            for (int i = 0; i < tempStr.split("\\.").length; i++) {

                tempList.add(count + " " + tempStr.split("\\.", i + 1)[i]);


            }


        }

        HashMap tempResult = new HashMap<String, Integer>();
        String[] key;
        for (String i : tempList) {
            key = i.split(" ");
            if ((Integer) tempResult.get(key[1]) != null)
                tempResult.put(key[1], (Integer) tempResult.get(key[1]) + Integer.valueOf(key[0]));
            else
                tempResult.put(key[1], Integer.valueOf(key[0]));

        }


        Iterator<String> iter1 = tempResult.keySet().iterator();

        List<String> result = new ArrayList<String>();

        while (iter1.hasNext()) {
            String temp = iter1.next();

            result.add(tempResult.get(temp) + " " + temp);

        }


        return result;
    }
}
