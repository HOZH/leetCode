import java.util.Arrays;
import java.util.HashSet;

public class test {


    public static void main(String[] args) {


        int[] nums1 = {1, 2, 3};
        int[] nums2 = {1, 2, 4};

        HashSet<Integer> set1 = new HashSet();
        HashSet<Integer> set2 = new HashSet();


        for (int i = 0; i < nums1.length; i++)
            set1.add(nums1[i]);
        for (int i = 0; i < nums1.length; i++)
            set2.add(nums2[i]);


        set1.retainAll(set2);


        System.out.println(set1);


        var set3 = Arrays.stream(set1.stream().toArray()).mapToInt(x -> (int) x).toArray();


        var set4 = set1.stream().mapToInt(x -> (int) x).toArray();
        System.out.println(set3);


        int k = 0;
        int[] answer = new int[set1.size()];
        for (int i : set1)

            answer[k++] = i;


    }


}