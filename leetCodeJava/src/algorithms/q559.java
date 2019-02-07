package algorithms;

import java.util.Iterator;
import java.util.List;

public class q559 {

    public int maxDepth(Node root) {

        if(root==null) return 0;
        int depth = 1;
        int temp;

        if (root.children != null && root.children.size() != 0) {
            Iterator<Node> iter = root.children.iterator();

            while (iter.hasNext()) {
                temp = maxDepth(iter.next()) + 1;
                if (temp > depth)
                    depth = temp;

            }
        }

        return depth;
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

    ;
}
