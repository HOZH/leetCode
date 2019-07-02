package amazon;

import java.util.Stack;

public class q1 {


    public static void main(String[] args) {


        var stack = new Stack<String>();


        stack.push("A");

        stack.push("B");

        stack.push("C");

        stack.push("D");


        for (int i = 0; i < 4; i++) {
            System.out.println(stack.pop());

        }


    }
}
