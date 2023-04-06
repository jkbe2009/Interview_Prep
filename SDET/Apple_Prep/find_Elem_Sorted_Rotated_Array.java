/*
* Click `Run` to execute the snippet below!
*/


import java.io.*;
import java.util.*;


/*
* To execute Java, please define "static void main" on a class
* named Solution.
*
* If you need more classes, simply define them inline.
*/


class Solution {
    public static void main(String[] args) {
    int[][] inp = {
        {1,2,3,4,5},
        {5,1,2,3,4},
        {4,5,1,2,3},
        {3,4,5,1,2},
        {2,3,4,5,1},
        {-1,-1,-1}
    };

    int key = 2;
    for (int[] inpVal : inp) System.out.println(findEl1(inpVal, key));
    System.out.println(" ");
    for (int[] inpVal : inp) System.out.println(findEl2(inpVal, key));
    }


    public static int findEl1(int[] a, int key){
        // Validate INput:
        if( a == null ||a.length == 0) throw new IllegalArgumentException("Invalid Input!!!");

        int pos = -1;

        int l = 0, r = a.length-1;

        while(l <= r){
            int m = (l + r)/2;

            if( key == a[m]) return m;

            //if left side is sorted
            else if(a[l] <= a[m]){
                // if key is present in the sorted side i.e left side
                if(key >= a[l] && key < a[m]) r = m-1;
                // else Go right
                else l = m+1;
            }
            
            //right side is sorted
            else{
                // if key is present in the sorted side i.e right side
                if(key > a[m] && key <= a[r]) l = m+1;
                // else Go left
                else r = m-1;
            }
        }

        return pos;
    }


    public static int findEl2(int[] a, int key){
        int min_pos = findMinEl(a);
        int pos = -1;

        pos = bSearch(a, key, 0, min_pos-1);
        if (pos == -1) pos = bSearch(a, key, min_pos, a.length-1);

        return pos;
    }


    public static int bSearch(int[] a, int key, int l, int r){
        //Base Case:
        if(l > r) return -1;

        if (l == r){
            if(a[l] == key) return l;
            else return -1;
        }

        //Recursive Case:
        int m = (l +r)/2;
        
        if(key == a[m]) return m;

        else if(key < a[m]) return bSearch(a, key, l, m-1);

        else return bSearch(a, key, m+1, r);
    }


    public static int findMinEl(int[] a){
        int l = 0, r = a.length-1;

        while (l<r){
            int m = (l+r)/2;

            if(a[m] < a[r]) r = m;

            else l = m+1;
        }

        return l;
    }
}
