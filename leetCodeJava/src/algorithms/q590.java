package algorithms;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class q590 {

    List<Integer> result = new ArrayList<>();

    public List<Integer> postorder(Node root) {



        if (root == null) return result;
        if (root.children == null || root.children.size() == 0) {
            result.add(root.val);
        } else {
            Iterator<Node> iter = root.children.iterator();


            while (iter.hasNext()) {

                postorder(iter.next());
            }

            result.add(root.val);
        }

        return result;
    }

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



}




