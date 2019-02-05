package algorithms;

import java.util.Arrays;
import java.util.OptionalInt;

public class q561 {


    public int arrayPairSum(int[] nums) {

        Arrays.sort(nums);


        int[] tempArr = new int[nums.length / 2];

        for (int i = 0; i < nums.length; i++) {
            if (i % 2 == 0) {

                tempArr[i / 2] = nums[i];
            }
        }

        OptionalInt temp = Arrays.stream(tempArr).reduce((a, b) -> (a + b));

        int answer=0;

        if (temp.isPresent()) {

            answer = temp.getAsInt();

        }

        return answer;
    }
}
