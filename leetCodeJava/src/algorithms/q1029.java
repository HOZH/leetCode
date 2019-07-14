package algorithms;

public class q1029 {

    public int twoCitySchedCost(int[][] costs) {


        int min = 0;
        int capacityOfEachCity = costs.length / 2;


        int[][] diff = new int[costs.length][2];


        int[] temp = null;


        for (int i = 0; i < costs.length; i++) {

            temp = costs[i];

            diff[i][0] = temp[0] - temp[1];
            diff[i][1] = i;

        }

        bubbleSort(diff);

        for (int i = 0; i < capacityOfEachCity; i++)

            min += costs[diff[i][1]][0];

        for (int i = capacityOfEachCity; i < costs.length; i++)

            min += costs[diff[i][1]][1];


        return min;


    }


    public void bubbleSort(int[][] target) {
        int in;
        int out;
        for (out = target.length - 1; out >= 1; out--) {
            for (in = 0; in < out; in++) {
                if (target[in][0] > target[in + 1][0]) {
                    swap(target, in, in + 1);
                }
            }
        }
    }

    private void swap(int[][] target, int num1, int num2) {


        int[] temp = target[num1];
        target[num1] = target[num2];
        target[num2] = temp;


    }

}
