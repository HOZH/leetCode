import java.util.Arrays;
import java.util.LinkedHashSet;

public class test {


    public static void main(String[] args) {


` `        int[] arr = {1, 2, 3, 2, 1, 6, 3, 4, 5, 2};


        arr = eliminateDuplicate(arr);

        for (int i : arr)
            System.out.println(i);

//        System.out.println(arr.toString());


    }


    static int[] eliminateDuplicate(int[] list) {


//        var temp_set = new HashSet<>();

        var temp_set = new LinkedHashSet<>();

        for (int i : list) {

            temp_set.add(i);


        }


//        var temp = new ArrayList<>();


//            var result = new int[temp_set.size()];


//        for(int i=0;i<temp_set.size();i++)
//            result[i]=temp_set.
//
//            result

        return Arrays.stream(temp_set.toArray()).mapToInt(t -> (int) t).toArray();


//        return null;
    }


}
