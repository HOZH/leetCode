package algorithms;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class q429 {

    class Node {
        public int val;
        public List<Node> children;

        public Node() {
        }

        public Node(int _val, List<Node> _children) {
            val = _val;
            children = _children;
        }
    }

    List<List<Integer>> list = new ArrayList<>();


    public List<List<Integer>> levelOrder(Node root) {

        if (root != null) {
            helper(root, 0);


            ArrayList<Integer> tempL = new ArrayList<>();
            tempL.add(root.val);
            if (list.size() == 0) {
                list.add(new ArrayList<>());
            }
            list.set(0, tempL);


        }


        return list;


    }


    void helper(Node root, int level) {

        if (root.children != null && root.children.size() != 0) {


            Iterator<Node> iter1 = root.children.iterator();


            while (iter1.hasNext()) {
                helper(iter1.next(), level + 1);
            }


            Iterator<Node> iter2 = root.children.iterator();

            while (iter2.hasNext()) {
                if ((level + 1) >= list.size()) {
                    while (list.size() <= level + 1)
                        list.add(new ArrayList<Integer>());
                    ArrayList<Integer> tempList = new ArrayList<>();
                    tempList.add(iter2.next().val);
                    list.set(level + 1, tempList);
                } else list.get(level + 1).add(iter2.next().val);
            }


        } else return;

    }


}
