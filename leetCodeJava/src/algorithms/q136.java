package algorithms;

import java.util.HashSet;

public class q136 {

    public int singleNumber(int[] nums) {

        HashSet set = new HashSet();
        HashSet moreThanOnce = new HashSet();


        int size;

        for (int i : nums) {
            size = set.size();
            set.add(i);
            if (size == set.size())
                moreThanOnce.add(i);

        }

        set.removeAll(moreThanOnce);


        return (int) set.iterator().next();


    }
}
