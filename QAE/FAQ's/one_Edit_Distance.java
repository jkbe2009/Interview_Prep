
import java.util.*;

class one_Edit_Distance{
    
    public static void main(String[] args) throws Exception {
        String[] inpArr = {
            {"abcd","acd"},
            {"acd","abcd"},
            {"abcd","abed"},
            {"abc","adb"},
            {"abc","adb"},
            {"abcde","abecd"}
        };

        for(String inp[] : inpArr){
            System.out.println(one_Edit_Distance (inp[0],inp[1]));
            System.out.println(one_Edit_Simple (inp[0],inp[1]));
        }
    }
    
    /*
    approach 1: long route

    find the difference between the length of s and t
    return false id its > 1
    if both are equal call method 1 to find is_true and return result
    if not equal find the smallest string call method 2 to find is_true and return result
    */   

    public static boolean one_Edit_Distance (String s, String t) {
        // O(n) || O(1)
        if (s == null || s.length()==0 || t == null || t.length()==0) return false;

        int lens = s.length(), lent = t.length();

        if ( abs(lens-lent) > 1) return false;

        if(Math.abs(lens-lent) == 0) return mod(s,t);

        else {
            if (lens < lent) return add_Del(s,t);
            else return add_Del(t,s);
        } 

    }


    public static boolean mod (String s1, String s2){

        boolean bFlag = false;
        for (int i =0; i< s1.length(); i++){

        if (s1.charAt(i) != s2.charAt(i)) {
            if (bFlag) return false;
        bFlag = true;
        }

        }

        return true;
    }

    public static boolean add_Del (String s1, String s2){

        for (int i =0; i<s2.length(); i++){
            if (s2.charAt(i) != s1.charAt(i)) {
                StringBuilder sb = new StringBuilder(s2);
                return s1.equals(sb.deleteCharAt(i).toString());
            }
        }

        return true;
    }


    /*
    approach 2: short route (combine both the functions)

    Loop using two pointers and traverse until the end of both the strings
    if the chars at these pointers don't match check if its first time
    if not return false
    else move the pointers accordingly
    end loop
    return true
    */   

    public static boolean one_Edit_Simple (String s, String t) {
        // O(n) || O(1)
        if (s == null || s.length()==0 || t == null || t.length()==0) return false;

        int slen = s.length(), slen = t.length();

        if (Math.abs(slen - tlen) >1) return false;

        String s1,s2;

        if (slen<tlen) {s1 = s; s2 = t;}
        else {s1 = t; s2 = s;}

        int i=0, j=0; boolean foundDiff = false;

        while ( i<s1.length() && j<s2.length()) {

            if (s1.charAt(i) != s2.charAt(j)){
                if (foundDiff) return false;
                if( s1.length() == s2.length() ) { i++; j++;}
                else { j++;}            
                foundDiff = true;
            }
            else { i++; j++;}
        }

        return true;
    }


}