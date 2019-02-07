package algorithms;

public class q806 {

    public int[] numberOfLines(int[] widths, String S) {


        char[] chars = S.toCharArray();
        int[] lens = new int[chars.length];

        for (int i = 0; i < chars.length; i++) {
            lens[i] = widths[chars[i] - 97];
        }


        int line = 1;
        int count = 0;


        for (int i = 0; i < lens.length; i++) {
            if (count + lens[i] <= 100)
                count += lens[i];
            else {
                count = lens[i];
                line++;
            }

        }
        int[] result = {line, count};
        return result;
    }
}
