package algorithms;

public class q344 {

    public void reverseString(char[] s) {

        char temp;
        for (int i = 0; i < s.length; i++) {
            if(i==s.length/2)
                break;
            temp = s[i];

            s[i] = s[s.length - 1 - i];

            s[s.length - 1 - i] = temp;


        }

    }
}
