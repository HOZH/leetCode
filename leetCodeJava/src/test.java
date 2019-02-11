import java.io.IOException;
import java.util.Arrays;
import java.util.List;
import java.util.Stack;

public class test {


    public static void main(String[] args) throws IOException {

//        List<Integer> tempList = new Stack<>();
//        var current = 6;
//        while (true) {
//
//            if (current % 2 == 00)
//                tempList.add(0);
//            else tempList.add(1);
//
//            current = current / 2;
//
//
//            if (current == 0)
//                break;
//
//
//        }
//
//        var str = "";
//        while (!tempList.isEmpty()) {
//            if (((Stack<Integer>) tempList).pop() == 1)
//                str += "1";
//            else
//                str += "0";
//
//        }
//
//
//        System.out.println(str);

        Arrays.stream("010".split("")).forEach(System.out::println);


    }
}

