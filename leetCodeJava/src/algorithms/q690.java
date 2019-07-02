package algorithms;

import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class q690 {
    class Employee {
        // It's the unique id of each node;
        // unique id of this employee
        public int id;
        // the importance value of this employee
        public int importance;
        // the id of direct subordinates
        public List<Integer> subordinates;
    }



    public int getImportance(List<Employee> employees, int id) {
        Employee root = null;
        for (
                Employee employee : employees) {
            if (employee.id == id) {
                root = employee;
                break;
            }
        }

        Queue<Employee> queue = new LinkedList<>();
        queue.offer(root);

        int result = 0;

        while (!queue.isEmpty()) {
            int numLevelNodes = queue.size();

            for (int i = 0; i < numLevelNodes; i++) {
                Employee node = queue.poll();
                result += node.importance;

                for (int subordinateID : node.subordinates) {

                    Employee subordinate = null;
                    for (Employee employee : employees) {
                        if (employee.id == subordinateID) {
                            subordinate = employee;
                            break;
                        }
                    }

                    queue.offer(subordinate);
                }
            }
        }

        return result;
    }
}
