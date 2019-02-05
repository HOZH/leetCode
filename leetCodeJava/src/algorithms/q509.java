package algorithms;

public class q509 {

    public int fib(int N) {

        int value = 0;

        if (N > 1) {

            value = fib(N - 1) + fib(N - 2);
        }

        if (N == 1) return 1;


        return value;


    }
}
