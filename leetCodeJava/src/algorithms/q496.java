package algorithms;

public class q496 {

    public int[] nextGreaterElement(int[] nums1, int[] nums2) {

        int[] result = new int[nums1.length];
        int temp = -1;


        for (int i = 0; i < nums1.length; i++) {

            for (int j = 0; j < nums2.length; j++) {

                if (nums2[j] == nums1[i]) {

                    for (int k = j; k < nums2.length; k++) {


                        if (nums2[k] > nums2[j]) {

                            temp = nums2[k];
                            break;
                        }

                    }


                    result[i] = temp;
                    temp = -1;

                    break;
                }

            }

        }

        return result;
    }
}
