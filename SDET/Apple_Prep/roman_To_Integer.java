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

        //String s = "XCIX"; //99
        String s = "CM"; //99
        System.out.println(rtoi(s));
    }


    public static int rtoi(String s){
        //Edge classes
        if (s == null || s == "" || s.length() ==0) throw new IllegalArgumentException("Invalid Input!!");

        int res = 0, prev = 0;

        Map<Character, Integer> map = new HashMap<>();

        map.put('I', 1);
        map.put('V', 5);
        map.put('X', 10);
        map.put('L', 50);
        map.put('C', 100);
        map.put('D', 500);
        map.put('M', 1000);

        for(int i = s.length()-1; i>=0; i--){
            char roman = s.charAt(i);
            int val = map.get(roman);
            if (val < prev) res -= val;
            else res += val;
            prev = val;
        }

        return res;
    }

}
