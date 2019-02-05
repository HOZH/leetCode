package algorithms;

import java.util.ArrayList;

public class q933 {


    ArrayList list = new ArrayList<Integer>();

    public q933() {


    }

    public int ping(int t) {

        list.add(t);


        return list.stream().filter(x -> (int) x <= t).filter(x -> (int) x >= t - 3000).mapToInt(x -> (int) x).toArray().length;

    }
}
