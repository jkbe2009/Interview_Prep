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
        //int i = 257;
        int i = 58;
        System.out.println(itor(i));
    }


    public static String itor(int num){
        //Edge case:
        if ( num <= 0 || num>4999) throw new IllegalArgumentException("Invalid I/P");


        StringBuilder sb = new StringBuilder();
        
        int[] a = new int[] {1,4,5,9,10,40,50,90,100,400,500,900,1000};
        String[] b = new String[]{"I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"};


        for(int i = a.length-1; i >=0; i--){
            if(a[i] <= num){
                while(num >= a[i]){
                    sb.append(b[i]);
                    num -= a[i];
                }
            }
        }


        return sb.toString();
    }
}


