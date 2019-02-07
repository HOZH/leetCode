package algorithms;

public class q700 {


    public q617.TreeNode searchBST(q617.TreeNode root, int val) {

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




