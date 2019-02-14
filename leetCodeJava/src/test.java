import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;
import java.util.Stack;

public class test {

    public static void main(String[] args) {


        List<Integer> tempList = new Stack<Integer>();
        int temp = 0;



        temp = 8;
        while (true) {

            if (temp % 2 == 00)
                tempList.add(0);
            else tempList.add(1);

            temp = temp / 2;


            if (temp == 0)
                break;


        }

        var str="";

        System.out.println(     ((Stack<Integer>) tempList).pop());
        System.out.println(     ((Stack<Integer>) tempList).pop());
        System.out.println(     ((Stack<Integer>) tempList).pop());
        System.out.println(     ((Stack<Integer>) tempList).pop());

        while(tempList.size()!=0)
        {
            str+=((Stack<Integer>) tempList).pop();
        }

    }

}