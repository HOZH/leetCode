package algorithms;

import java.util.List;
import java.util.Stack;

public class q762 {

    public int countPrimeSetBits(int L, int R) {


        int count = 0;
        int ones = 0;
        List<Integer> tempList = new Stack<Integer>();
        int temp = 0;
        StringBuilder str =new StringBuilder();

        for (int i = L; i <= R; i++) {


            temp = i;
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


            str = new StringBuilder();

            for (int j = 0; j < chars.length; j++) {


                if (chars[j] == '1')
                    ones++;

            }

            if (ones == 2) {

                count++;


            } else {
                for (int j = 2; j < ones; j++) {

                    if (ones % j == 0)
                        break;

                    if (ones == j + 1) {
                        count++;
                    }
                }


            }
            ones = 0;
        }


        return count;
    }
}
