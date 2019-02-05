import algorithms.*;

import java.util.Arrays;


public class test{


    public static void main(String[] args) {


       var a = new q973();

       int [][] b ={{1,3},{-2,2}};


        Arrays.stream(a.kClosest(b, 1)[0]).forEach(System.out::println);
    }
}