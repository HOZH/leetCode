package algorithms;

public class q657 {


    public boolean judgeCircle(String moves) {

        int x = 0;
        int y = 0;
        char[] orders = moves.toCharArray();

        for (char c : orders) {
            switch (c) {

                case ('D'):
                    --y;
                    break;


                case ('U'):
                    ++y;
                    break;


                case ('R'):
                    ++x;
                    break;

                case ('L'):
                    --x;
                    break;

                default:
                    break;

            }


        }

        return (x == 0) && (y == 0);


    }
}
