package algorithms;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class q821 {

    public int[] shortestToChar(String S, char C) {

        List occ = new ArrayList<Integer>();
        char[] chars = S.toCharArray();

        for (int i = 0; i < chars.length; i++) {

            if (chars[i] == C)

                occ.add(i);

        }

        int[] result = new int[chars.length];

        int min = 999;
        int current = 0;
        Iterator<Integer> iter;


        for (int i = 0; i < chars.length; i++) {
            min = 999;
            current = 0;

            iter = occ.iterator();
            while (iter.hasNext()) {
                current = Math.abs(iter.next() - i);

                if (min > current) {

                    min = current;
                }


            }
            result[i] = min;

        }


        return result;
    }


}
