package algorithms;

public class q206 {

    public class ListNode {
        int val;
        ListNode next;

        ListNode(int x) {
            val = x;
        }
    }

    public ListNode reverseList(ListNode head) {

        if (head == null)
            return head;

        ListNode a, b, c;

        a = head;
        c = null;
        while (true) {


            b = a.next;

            a.next = c;

            if (b == null)
                return a;
            c = a;
            a = b;


        }


    }
}
