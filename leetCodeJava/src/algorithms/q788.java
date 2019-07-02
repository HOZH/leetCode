package algorithms;

public class q788 {

    public int rotatedDigits(int N) {

        int temp, current, count;

        count = 0;


        boolean flag = false;

        for (int i = 1; i < N + 1; i++) {


            temp = i;

            while (true) {

                if (temp / 10 != 0) {

                    current = temp % 10;


                    if (current == 2 || current == 5 || current == 6 || current == 9) {
                        flag = true;

                        temp /= 10;
                    } else if (current == 0 || current == 1 || current == 8) {
                        temp /= 10;
                    } else {

                        flag = false;
                        break;
                    }

                } else {
                    if (temp != 2 && temp != 5 && temp != 6 && temp != 9) {

                        if (temp != 0 && temp != 1 && temp != 8)
                            flag = false;

                        if (flag)
                            count++;


                    } else
                        count++;


                    flag = false;
                    break;


                }
            }
        }
        return count;
    }
}
