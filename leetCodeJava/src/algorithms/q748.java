package algorithms;

import java.util.HashMap;

public class q748 {

    public String shortestCompletingWord(String licensePlate, String[] words) {


        int index = -1;


        char[] keys = licensePlate.toLowerCase().toCharArray();
        HashMap<Character, Integer> map = new HashMap();


        for (char i : keys) {

            if (i >= 97 && i <= 122) {

                if (map.containsKey(i))
                    map.put(i, map.get(i) + 1);
                else
                    map.put(i, 1);
            }
        }


        HashMap<Character, Integer> copy = new HashMap(map);


        for (int k = 0; k < words.length; k++) {


            char[] chars = words[k].toCharArray();

            for (int j = 0; j < chars.length; j++) {

                char i = chars[j];

                if (map.containsKey(i)) {

                    if (map.get(i) == 1) {
                        map.remove(i);


                    } else
                        map.put(i, map.get(i) - 1);

                    if (map.isEmpty()) {

                        if (index == -1) {
                            index = k;
                            break;

                        }


                        if (words[k].length() < words[index].length())
                            index = k;


                    }
                }
            }

            map = new HashMap<>(copy);

        }

        return words[index];
    }
}
