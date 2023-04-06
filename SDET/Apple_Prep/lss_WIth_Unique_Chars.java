    /*
* Click `Run` to execute the snippet below!
*/


import java.io.*;
import java.util.*;


import org.w3c.dom.ls.LSSerializer;




/*
* To execute Java, please define "static void main" on a class
* named Solution.
*
* If you need more classes, simply define them inline.
*/


class Solution {
    public static void main(String[] args) {
        
        String s = "aaabcaa";

        System.out.println(ls(s));
        System.out.println(lss(s));
    }


    public static int ls(String s){
        //EDGE CASE:
        if ( s == null || s. length() == 0 || s == "") throw new IllegalArgumentException("Invalid I/p");
        int max_len = 0, len = 1;

        int l = 0;

        Set<Character> set = new HashSet<>();
        set.add(s.charAt(0));

        for (int r = 1; r< s.length()-1; r++){
            while(set.contains(s.charAt(r))){
                set.remove(s.charAt(l));
                l++;
            }

            set.add(s.charAt(r));

            len = r-l+1;

            max_len = Math.max(max_len, len);

        }

        return max_len;
    }


    public static String lss(String s){
        //EDGE CASE:
        if ( s == null || s. length() == 0 || s == "") throw new IllegalArgumentException("Invalid I/p");
        int max_len = 1, len = 1;
        String lStr = s.charAt(0) + "";

        int l = 0;

        Set<Character> set = new HashSet<>();
        set.add(s.charAt(0));

        for (int r = 1; r< s.length()-1; r++){
            while(set.contains(s.charAt(r))){
                set.remove(s.charAt(l));
                l++;
            }

            set.add(s.charAt(r));

            len = r-l+1;

            //max_len = Math.max(max_len, len);

            if (len > max_len) {
                lStr = s.substring(l,r+1);
                max_len = len;
            }
        }

        return lStr;
    }
}


