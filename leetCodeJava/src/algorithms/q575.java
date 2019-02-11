package algorithms;

import java.util.HashSet;

public class q575 {

    public int distributeCandies(int[] candies) {

        int num = candies.length;



        HashSet container = new HashSet();

        for (int i = 0; i < candies.length; i++) {

            container.add(candies[i]);
        }

        int kinds = container.size();





        if(kinds>num/2)
           return num/2;
        else return kinds;


    }

}
