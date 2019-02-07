package algorithms;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class q589 {

    List<Integer> result = new ArrayList<>();

    public List<Integer> preorder(q590.Node root) {


        if (root == null) return result;

        result.add(root.val);

        Iterator<q590.Node> iter = root.children.iterator();

        while (iter.hasNext()) {

            preorder(iter.next());

        }


        return result;
    }


}
