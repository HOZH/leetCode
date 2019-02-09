package algorithms;

import java.util.ArrayList;

public class q872 {

    class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode(int x) {
            val = x;
        }
    }

    ArrayList<Integer> list1 = new ArrayList<>();
    ArrayList<Integer> list2 = new ArrayList<>();

    public boolean leafSimilar(TreeNode root1, TreeNode root2) {

        getLeafValueSeq(root1, list1);
        getLeafValueSeq(root2, list2);


        boolean answer = true;

        if (list1.size() != list2.size()) return false;
        else {
            for (int i = 0; i < list1.size(); i++) {
                if (list1.get(i) != list2.get(i)) {
                    answer = false;
                    break;
                }
            }


        }
        return answer;
    }

    private void getLeafValueSeq(TreeNode head, ArrayList<Integer> list) {

        if (head == null) return;

        if (head.left == null && head.right == null) {
            list.add(head.val);


        } else if (head.left != null && head.right != null) {
            getLeafValueSeq(head.left, list);
            getLeafValueSeq(head.right, list);
        } else if (head.left != null)
            getLeafValueSeq(head.left, list);
        else if (head.right != null)
            getLeafValueSeq(head.right, list);

    }
}
