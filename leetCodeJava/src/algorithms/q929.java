package algorithms;

import java.util.HashSet;

public class q929 {

    public static void main(String[] args) {

        var email1 = "o?+n.c?e@upon.com";
        var email2 = "oa?+n.c?e@upon.com";
        var emails = new String[2];
        emails[0] = email1;
        emails[1] = email2;
        System.out.println(numUniqueEmails(emails));

    }

    public static int numUniqueEmails(String[] emails) {


        HashSet tempSet = new HashSet<String>();
        for (String email : emails) {

            String[] tempArr = email.split("@");
            String local = tempArr[0];
            String domain = tempArr[1];


            tempSet.add(local.replace(".", "").split("\\+")[0] + "@" + domain);


        }


        return tempSet.size();
    }
}
