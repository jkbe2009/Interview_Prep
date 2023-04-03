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
        int[] inp = new int[] {1,3,5,7,8,9,12,15};
        int key = 7;
        System.out.println(bSearchRec(inp, key, 0, inp.length-1));
        System.out.println(bSearchItr(inp, key));
        key = 6;
        System.out.println(bSearchRec(inp, key, 0, inp.length-1));
        System.out.println(bSearchItr(inp, key));
    }


    public static int bSearchRec(int[] inp, int key, int l, int r){
        //Base case:
        if (l == r) {
            if (inp[l] == key) return l;
            else return -1;
        }

        //Rec case:
        int m = (l+r)/2; 

        if (key == inp[m]) return m;
        else if (key < inp[m]) return bSearchRec(inp, key, l, m-1);
        else return bSearchRec(inp, key, m+1, r);

    }


    public static int bSearchItr(int[] inp, int key){

        int l = 0;
        int r = inp.length-1;

        while (l<=r){
            
            int m = (l+r)/2;

            if(key == inp[m]) return m;

            else if (key < inp[m]) r = m-1;

            else l = m+1;

        }

        return -1;
    }

}


