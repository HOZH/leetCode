package algorithms;

public class q852 {


    public int peakIndexInMountainArray(int[] A) {

        int peak=0;


        for(int i =0;i<A.length-1;i++){

            if(A[i]<A[i+1]){
                peak++;
            }
        }


        return peak;
    }
}
