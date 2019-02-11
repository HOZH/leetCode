package algorithms;

import java.util.Arrays;
import java.util.List;
import java.util.Stack;

public class q868 {

    public int binaryGap(int N) {

        int distance = 0;
        int index1;
        int index2=0;

        List<Integer> tempList = new Stack<>();
        int current = N;
        while (true) {

            if (current % 2 == 00)
                tempList.add(0);
            else tempList.add(1);

            current = current / 2;


            if (current == 0)
                break;


        }

        StringBuilder str = new StringBuilder();
        while (!tempList.isEmpty()) {
            if (((Stack<Integer>) tempList).pop() == 1)
                str.append(1);
            else
                str.append(0);
        }
        int[] ints = Arrays.stream(str.toString().split("")).mapToInt(x -> Integer.valueOf(x)).toArray();


        for (int i = 0; i < ints.length; i++) {

            if (ints[i] == 1) {
                index1 = index2;
                index2 = i;
                distance = (distance < index2 - index1) ? index2 - index1 : distance;

            }

        }


        return distance;
    }
}
