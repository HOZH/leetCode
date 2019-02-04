package algorithms;

import java.util.Arrays;

public class q977 {


    public int[] sortedSquares(int[] A) {


//        int[] result = Arrays.stream(A).map(x -> (int) Math.pow(Math.abs(x), 2)).toArray();

//        String[] a= Arrays.stream(strs).filter(someCondition1).map(Object::toString).toArray(String[]::new);


//        var temp= Arrays.stream(result).boxed().toArray(Integer[]::new);
//        System.out.println(temp.getClass().getName());
//        Arrays.sort(temp, Collections.reverseOrder());
//      result= Arrays.stream(temp).mapToInt(i->i).toArray();

        int[] result = Arrays.stream(A).map(x -> (int) Math.pow(Math.abs(x), 2)).toArray();
        Arrays.sort(result);
        return result;


    }
}
