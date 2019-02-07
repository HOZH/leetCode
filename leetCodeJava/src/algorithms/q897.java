package algorithms;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class q897 {

    List values = new ArrayList<Integer>();

    public TreeNode increasingBST(TreeNode root) {

        if (root != null) {


            if (root.left != null)
                increasingBST(root.left);

            values.add(root.val);

            if (root.right != null)
                increasingBST(root.right);
        }

        Iterator<Integer> iter = values.iterator();

        TreeNode currentNode = null;

        if (iter.hasNext()) {
            root = new TreeNode(iter.next());
            currentNode = root;
        }
        while (iter.hasNext()) {

            currentNode.right = new TreeNode(iter.next());

            currentNode = currentNode.right;


        }

        return root;


    }

    class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode(int x) {
            val = x;
        }
    }
}
