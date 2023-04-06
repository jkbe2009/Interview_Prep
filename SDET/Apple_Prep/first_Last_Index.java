
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
        int[] inp = {1,2,3,3,4,4,4,4,5,6};

        int[] res = find(inp, 4);
        System.out.println(res[0] + "," +res[1]);

        res = find(inp, 8);
        System.out.println(res[0] + "," +res[1]);
    }


    public static int[] find(int[] a, int key){
        //Validate Input:
        if(a == null || a.length == 0) throw new IllegalArgumentException("Invalid Input!!!");

        int[] res = new int[] {-1, -1};

        res[0] = findFirst(a, key);
        if (res[0] != -1) res[1] = findLast(a, key);

        return res;
    }




    public static int findFirst(int[] a, int key){
        int l = 0, r = a.length-1;
        int first = -1;

        while(l <= r){
            int m = (l+r)/2;

            if(a[m] == key){
                first = m;
                r = m-1;
            }

            else if(key < a[m]) r = m-1;

            else l = m+1;
        }

        return first;
    }


    public static int findLast(int[] a, int key){
        int l = 0, r = a.length-1;
        int last = -1;

        while(l <= r){
            int m = (l+r)/2;

            if(a[m] == key){
                last = m;
                l = m+1;
            }

            else if(key < a[m]) r = m-1;

            else l = m+1;
        }

        return last;
    }
}
