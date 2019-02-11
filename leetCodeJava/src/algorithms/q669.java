package algorithms;

public class q669 {

    class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode(int x) {
            val = x;
        }
    }


    private TreeNode helper(TreeNode root, int L, int R) {
        TreeNode current;


        if (root.left != null) {

            current = root.left;
            if (current.val > R) {

                if (current.left != null) {

                    root.left = current.left;


                }


            }
            root.left = trimBST(root.left, L, R);

        }

        if (root.right != null) {

            current = root.right;
            if (current.val < L) {

                if (current.right != null) {

                    root.right = current.right;


                }


            }

            root.right = trimBST(root.right, L, R);
        }

        if (root.val < L) {
            if (root.right != null)
                root = root.right;
            else {
                return null;
            }
        } else if (root.val > R) {
            if (root.left != null)
                root = root.left;
            else {
                return null;
            }
        }

        return root;
    }

    public TreeNode trimBST(TreeNode root, int L, int R) {


        if (root == null) {
            return null;
        } else return helper(root, L, R);

    }

}


