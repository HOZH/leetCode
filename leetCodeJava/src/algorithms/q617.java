package algorithms;


public class q617 {

    public TreeNode mergeTrees(TreeNode t1, TreeNode t2) {


        if (t1 == null && t2 != null) {
            t1 = new TreeNode(t2.val);
            t1.left = t2.left;
            t1.right = t2.right;
            t2 = null;
        } else if (t1 != null && t2 != null) {
            t1.val = t1.val + t2.val;
        } else if (t2 != null) {
            t1.val = t2.val;
        } else if (t2 == null) {
            return t1;
        } else return null;


        if (t1 != null && t2 != null) {


            if (t1.left == null && t2.left != null) {

                t1.left = t2.left;
                mergeTrees(t1.left, null);
            } else {
                mergeTrees(t1.left, t2.left);
            }


            if (t1.right == null && t2.right != null) {

                t1.right = t2.right;
                mergeTrees(t1.right, null);
            } else {
                mergeTrees(t1.right, t2.right);
            }
        } else if (t2 != null) {

            t1 = new TreeNode(t2.val);
            t1.left = t2.left;
            t1.right = t2.right;
            t2 = null;
        }


        return t1;
    }


    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode(int x) {
            val = x;
        }
    }
}
