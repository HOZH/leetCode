package algorithms;

public class q226 {

    public TreeNode invertTree(TreeNode root) {

        if (root != null) {
            TreeNode tempNode;
            if (root.left != null || root.right != null) {
                tempNode = root.left;
                root.left = root.right;
                root.right = tempNode;
            }

            if (root.left != null)
                invertTree(root.left);
            if (root.right != null)
                invertTree(root.right);


            return root;
        }

        return null;

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
