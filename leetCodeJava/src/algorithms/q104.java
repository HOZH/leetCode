package algorithms;

public class q104 {

    class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode(int x) {
            val = x;
        }
    }


    private int helper(TreeNode root) {

        int len = 0;

        if (root.left != null || root.right != null)
            len = 1;

        int a, b;
        a = b = 0;
        if (root.left != null)
            a = helper(root.left);
        if (root.right != null)
            b = helper(root.right);

        len = a > b ? len + a : len + b;

        return len;
    }

    public int maxDepth(TreeNode root) {

if(root!=null)
        return 1 + helper(root);
else return 0;

    }
}
