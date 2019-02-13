import java.io.IOException;
import java.util.ArrayList;

public class test {


    static int b;

    public static void main(String[] args) throws IOException {





        var a = new ArrayList<Integer>();


        System.out.println(a.size());

//        System.out.println(a.get(0)==null);
a.add(1);


        System.out.println(a.get(0));

        a.set(0,2);

        System.out.println(a.get(0));



    }

}