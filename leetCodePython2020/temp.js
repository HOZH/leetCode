// var flatten = function(root) {
//     let curr = root;
//     // Utilize Morris Traversal 
//     // Walk through tree so long as current node is defined
    
//     while (curr) {
//         if (curr.left) {
//             // If left node exists set the guide to left
//             let guide = curr.left;
            
//             // Guide should traverse until all the way to right
//             while (guide.right) guide = guide.right;
            
//             guide.right = curr.right;
//             curr.right = curr.left;
//             curr.left = null;
//         }
//         // Otherwise continue right
//         curr = curr.right;
//     }
// };


// Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
// and return an array of the non-overlapping intervals that cover all the intervals in the input.


// Input: intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
// Output: [[1, 6], [8, 10], [15, 18]]
// Explanation: Since intervals[1, 3] and [2, 6] overlaps, merge them into[1, 6].


// Input: intervals = [[1, 4], [4, 5]]
// Output: [[1, 5]]
// Explanation: Intervals[1, 4] and [4, 5] are considered overlapping.


// Constraints:

// 1 <= intervals.length <= 104
// intervals[i].length == 2
// 0 <= starti <= endi <= 104


var merge = function(intervals) {
    if (intervals.length < 2) return intervals;
    
    // Sort intervals by first num of set
    intervals = intervals.sort((a, b) => a[0] - b[0]); // [[1, 4], [4, 5]]
    
    const result = [];
    let prev = intervals[0]; // [1, 4]
    
    // Compare if current set begins after previous set ends
    for (let i = 1; i < intervals.length; i++) {
        // Compare "4" in [1, 4] with "4" in [4, 5]
        // If last num in prev: "4" is greater or equal than first num "4" in next
        if (prev[1] >= intervals[i][0]) {
            // Override previous' end number "4" in [1, 4] with last num "5" in [4, 5]
            prev = [prev[0], Math.max(prev[1], intervals[i][1])]
        } else {
            // Otherwise push the previous set;
            // pushes prev = [1, 5] into result
            // Res = [[1, 5]]
            // Update previous to be curr
            result.push(prev);
            prev = interval[i];
        }
    }

    result.push(prev);

    return result;
};