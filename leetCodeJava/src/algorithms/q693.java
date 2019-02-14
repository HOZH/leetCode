package algorithms;

import java.util.List;
import java.util.Stack;

public class q693 {


    public boolean hasAlternatingBits(int n) {

        List<Integer> tempList = new Stack<Integer>();
        int temp = 0;
        StringBuilder str = new StringBuilder();


        temp = n;
        while (true) {

            if (temp % 2 == 00)
                tempList.add(0);
            else tempList.add(1);

            temp = temp / 2;


            if (temp <= 0)
                break;


        }

        while (tempList.size() != 0) {
            str.append(((Stack<Integer>) tempList).pop());
        }


        char[] chars = str.toString().toCharArray();


        for (int i = 0; i < chars.length - 1; i++) {

            if (chars[i] == chars[i + 1]) {
                return false;
            }
        }


        return true;
    }
}

