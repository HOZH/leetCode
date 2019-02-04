package algorithms;

import java.util.HashSet;

public class q961 {


    public int repeatedNTimes(int[] A) {


        int before = 0;
        int after = 0;

        HashSet container = new HashSet();
        for (int a : A) {

            before = container.size();

            container.add(a);

            after = container.size();

            if (before == after)

                return a;


        }


        return 0;
    }
}
