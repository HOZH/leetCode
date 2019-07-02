package algorithms;

public class q258 {

    public int helper(int n) {
        int sum = 0;
        int buffer = 0;
        int temp = n;
        while (true) {
            if (temp / 10 != 0) {

                buffer = temp % 10;
                temp /= 10;
                sum += buffer;
            } else {
                sum += temp;
                break;
            }
        }

        return sum;
    }

    public int addDigits(int num) {

        int answer = helper(num);

        while (true) {
            if (answer / 10 != 0) {

                answer = helper(answer);
            } else break;

        }


        return answer;


    }
}
