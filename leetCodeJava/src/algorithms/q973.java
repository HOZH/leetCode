package algorithms;

import java.util.Arrays;
import java.util.HashMap;

public class q973 {

    public int[][] kClosest(int[][] points, int K) {


        int[][] tempArr = new int[points.length][2];

        HashMap container = new HashMap<Integer, int[]>();


        for (int[] i : points) {
            container.put((int) (Math.pow(i[0], 2) + Math.pow(i[1], 2)), i);

        }
        System.out.println(container.keySet());
        Object indices = container.keySet().stream().mapToInt(x -> (int) x).toArray();

        Arrays.sort((int[]) indices);

        int[][] answer = new int[K][2];


        for (int i = 0; i < K; i++) {
            answer[i] = (int[]) container.get(((int[]) indices)[i]);
        }


        return answer;


    }
}
