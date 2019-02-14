package algorithms;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

public class q637 {

    List<List<Long>> list = new ArrayList<>();
    List<Double> result = new ArrayList<>();

    public List<Double> averageOfLevels(TreeNode root) {

        if (root != null) {
            helper(root, 0);


            ArrayList<Long> tempL = new ArrayList<>();
            tempL.add(Long.valueOf(root.val));
            if (list.size() == 0) {
                list.add(new ArrayList<>());
            }
            list.set(0, tempL);

            Double tempDouble;
            long templong = 0;


            result = new ArrayList<>();

            while (result.size() < list.size()) {
                result.add(0.0);
            }


            for (int i = 0; i < list.size(); i++) {


                Optional<Long> j = list.get(i).stream().reduce((x, y) -> (x + y));

                if (j.isPresent()) {

                    templong = j.get().longValue();

                }

                tempDouble = (double) templong / (double) list.get(i).size();


                result.set(i, tempDouble);

            }


        }


        return result;


    }

    void helper(TreeNode root, int level) {

        if (root.left != null || root.right != null) {


            if ((level + 1) >= list.size()) {
                while (list.size() <= level + 1) {
                    list.add(new ArrayList<>());
                }


            }

            if (root.left != null) {
                list.get(level + 1).add(Long.valueOf(root.left.val));
                helper(root.left, level + 1);


            }

            if (root.right != null) {
                helper(root.right, level + 1);
                list.get(level + 1).add(Long.valueOf(root.right.val));


            }

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


}
