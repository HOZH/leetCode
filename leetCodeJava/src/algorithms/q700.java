package algorithms;

public class q700 {


    public TreeNode searchBST(TreeNode root, int val) {

        if (val == root.val) {
            return root;
        } else if (val > root.val) {

            if (root.right != null)
                return searchBST(root.right, val);
        } else if (val < root.val) {
            if (root.left != null)
                return searchBST(root.left, val);
        }


        return null;
    }

}


class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) {
        val = x;
    }
}
