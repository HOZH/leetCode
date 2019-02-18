package algorithms;

public class q521 {

    public int findLUSlength(String a, String b) {

        int aLen = a.length();
        int bLen = b.length();

        if (aLen == bLen) {
            if (a.equals(b)) {
                return -1;
            } else return aLen;
        } else return aLen > bLen ? aLen : bLen;


    }
}
