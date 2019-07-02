package algorithms;

import java.util.HashSet;

public class q349 {
    public int[] intersection(int[] nums1, int[] nums2) {

        HashSet<Integer> set1 = new HashSet();
        HashSet<Integer> set2 = new HashSet();


        for (int i = 0; i < nums1.length; i++)
            set1.add(nums1[i]);
        for (int i = 0; i < nums2.length; i++)
            set2.add(nums2[i]);


        set1.retainAll(set2);


        int k = 0;
        int[] answer = new int[set1.size()];
        for (int i : set1)

            answer[k++] = i;


        // return set1.stream().mapToInt(x->(int)x).toArray();

        return answer;

    }
}
