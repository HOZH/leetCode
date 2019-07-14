package algorithms;

public class q696 {

    public int countBinarySubstrings(String s) {


        int count = 0;

        char[] chars = s.toCharArray();

        int first, second;

        int firstLen = 0;

        first = 0;
        second = 0;

        char key;

        int temp = 0;

//        boolean firstHalf = true;

        for (int i = 0; i < chars.length; i++) {


            if (temp != 0) {

                temp--;
                continue;
            }

            key = chars[i];
            firstLen = 0;

            for (int j = i; j < chars.length; j++) {

                if (chars[j] == key) {
                    first++;
                    firstLen++;
                } else if (chars[j] != key) {

                    key = chars[j];


//                    System.out.println(firstLen);
                    for (int k = j; k < (j + firstLen); k++) {


                        if (k >= chars.length) {
                            firstLen = 0;
                            break;
                        }
                        if (chars[k] == key)
                            second++;
                        else {

                            break;
                        }

                        if (second == first && first != 0) {
                            count += second;
                            temp = second - 1;
                        }
//                        System.out.println(second);


                    }


                    break;

                }


            }

            first = 0;
            second = 0;
            firstLen = 0;
        }

        return count;
    }
}
