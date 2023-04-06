
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

        int[] arr = {2,2,2,2,3,3,3,3,2};

        System.out.println(majEl(arr));
    }


    public static int majEl(int[] inp){
        // Edge case:
        if(inp == null || inp.length == 0) throw new IllegalArgumentException("Invalid Inp!!!");

        int maj_el = -1, max_count = Integer.MIN_VALUE;

        Map<Integer, Integer>  map = new LinkedHashMap<>();

        int n = (inp.length)/2;

        for(int i :inp)
            map.put(i, map.getOrDefault(i, 0)+1);
        
        for(Map.Entry<Integer,Integer> entry : map.entrySet()){
            int v = entry.getValue();
            if(v > max_count){
                maj_el= entry.getKey();
                max_count = v;
            }
        }

        return (max_count > n) ? maj_el : -1;
    }

}




