package algorithms;

import java.util.List;
import java.util.Stack;

public class q476 {

    public int findComplement(int num) {


        List<Integer> tempList = new Stack<Integer>();


        int current = num;


        while (true) {

            if (current % 2 == 00)
                tempList.add(0);
            else tempList.add(1);

            current = current / 2;


            if (current == 0)
                break;


        }


        String str = "";

        while (!tempList.isEmpty()) {
            if (((Stack<Integer>) tempList).pop() == 1)
                str += "0";
            else
                str += "1";

        }


        char[] chars = str.toCharArray();


        int tempResult = 0;


        for (int i = 0; i < chars.length; i++) {

            tempResult += (chars[i] - 48) * Math.pow(2, chars.length - 1 - i);
        }


        return tempResult;
    }
}
