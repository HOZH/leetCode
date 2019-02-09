package algorithms;

import java.util.Stack;

public class q682 {

    public int calPoints(String[] ops) {

        int current = 0;
        int temp = 0;
        int temp1 = 0;
        String tempStr;
        Stack<Integer> records = new Stack<>();

        for (int i = 0; i < ops.length; i++) {
            tempStr = ops[i];
            if (tempStr.equals("C")) {

                current = current - records.pop();

            } else if (tempStr.equals("D")) {
                current = current + records.peek() * 2;
                records.push(records.peek() * 2);


            } else if (tempStr.equals("+")) {
                temp = records.pop();
                temp1 = records.peek() + temp;

                current = current + temp1;
                records.push(temp);
                records.push(temp1);

            } else {


                temp = Integer.valueOf(ops[i]);
                current = current + temp;
                records.push(temp);

            }

        }
        return current;
    }
}
