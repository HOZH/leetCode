package algorithms;

public class q485 {

    public int findMaxConsecutiveOnes(int[] nums) {

        int current, count;

        current = count = 0;

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 0) {

                if (current > count)
                    count = current;

                current = 0;
            } else
                current++;
        }



        return current > count ? current : count;

    }
}
