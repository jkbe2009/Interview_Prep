
import java.util.*;

class rotate_Array{
    
    public static void main(String[] args) throws Exception {
        int[] inpArr = { 1, 2, 3, 4, 5};
        int[] inpArr1 = new int[inpArr.length];

        for(int i= 0; i<=inpArr.length; i++){
            System.arraycopy(inpArr, 0, inpArr1, 0, inpArr.length);
            rotate(inpArr1,i);
            System.out.println(Arrays.toString(inpArr1));
        } 

        for (int i = 0; i <= inpArr.length; i++) {
            System.arraycopy(inpArr, 0, inpArr1, 0, inpArr.length);
            rotate_InPlace(inpArr1, i);
            System.out.println(Arrays.toString(inpArr1));
        }
     
    }
    
    /*
     * approach 1: Additional array
     * create an add array copy elements from n-1-k to n-1 
     * and then copy the remaining elements after that 
     * copy the new array back to original array and return
     * 
     */   

     public static void rotate (int[] a, int k){
        //O(n) || O(n)
        if( a == null || a.length == 0) throw new IllegalArgumentException("Invalid Input");

        int len = a.length;
        k = k%len;
        if (k == 0) return;
        int[] b = new int[len];

        int j=0;
        for(int i=k; i<len; i++){
        b[j++]= a[i];
        }
        for(int i=0; i<k; i++){
        b[j++]= a[i];
        }

        System.arraycopy(b,0,a,0,len);
        return;
    }
    
    /*
     * approach 2: Reversal - In place 
     * reverse the first k elements in the array in-place 
     * reverse the elements elements in the array in-place 
     * reverse the entire array in-place 
     */

    public static void rotate_InPlace (int[] a, int k){
        //O(n) || O(1)
        if( a == null || a.length == 0) throw new IllegalArgumentException("Invalid Input");

        int len = a.length;
        k = k%len;
        if (k == 0) return;

        reverse(a,0,k-1);
        reverse(a,k,len-1);
        reverse(a,0,len-1);

        return;
    }

    public static void reverse(int[] a, int i, int j) {

        while (i < j) {
            int temp = a[i];
            a[i] = a[j];
            a[j] = temp;
            i++;
            j--;
        }

        return;
    }

}


