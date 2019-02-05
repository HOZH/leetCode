package algorithms;

public class q965 {

    public boolean isUnivalTree(q617.TreeNode root) {

        boolean isUni = true;
        boolean isUni1 = true;
        boolean isUni2 = true;

        if (root.right != null) {
            if (root.val != root.right.val)
                return false;
        }

        if (root.left != null) {
            if (root.val != root.left.val)
                return false;
        }

        if (root.left != null)
            isUni1 = isUnivalTree(root.left);

        if (root.right != null)
            isUni2 = isUnivalTree(root.right);

        if (!isUni1 || !isUni2) {
            isUni = false;
        }

        return isUni;
    }
}
