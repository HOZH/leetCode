package algorithms;

public class q876 {


    int len = 0;

    public ListNode middleNode(ListNode head) {

        ListNode answer = head;
        len++;
        if (head.next != null) {

            middleNode(head.next);

        }


        for (int i = 0; i < len / 2; i++) {

            if (answer.next != null)
                answer = answer.next;

        }

        return answer;

    }

    class ListNode {
        int val;
        ListNode next;

        ListNode(int x) {
            val = x;
        }
    }
}
