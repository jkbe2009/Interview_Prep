
import java.util.*;

class binary_Search{
    
    public static void main(String[] args) throws Exception {
    int[] inpArr = {1,3,6,9,10,15,18,24};
    int key = 18;

    System.out.println(bSearch_Iter (inpArr, key));
    System.out.println(bSearch_Rec (inpArr, key, 0, inpArr.length-1));
    
    }
    
    /*
     * Use two pointers l at 0 and r at n-1 
     * while l<=r 
     * check if m = (l+r)/2 contains the key return m 
     * else move l and r pointers based on a[m] w.r.t key
     */   

     public static int bSearch_Iter(int[] a, int key) {
        // O(logn) || O(1)

        if (a == null || a.length == 0)
            return -1;

        int l = 0, r = a.length - 1;

        while (l <= r) {
            int m = l + (r - l) / 2;

            if (key == a[m])
                return m;
            else if (key < a[m])
                r = m - 1;
            else
                l = m + 1;
        }
        
        return -1;
     }

    /*
     * Use two parameters l and r
     * if l ==r check if a[m] == key return m else return -1
     * check if m = (l+r)/2 contains the key return m 
     * else set l and r based on a[m] w.r.t key and call the method recursively
     * 
     */     

     public static int bSearch_Rec (int[] a, int key, int l, int r){
        // O(logn) || O(logn)

        //Base case
        if (l == r) {
            if (a[l] == key) return l;
            else return -1;
        }

        //Recursive case:
        int m = l + (r - l) / 2;

        if (key == a[m]) return m;
        else if (key < a[m]) return bSearch_Rec (a, key, l, m-1);
        else return bSearch_Rec (a, key, m+1, r);

        }

}


