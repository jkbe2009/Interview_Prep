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

        String s = "hello123 w orld!@#";
        System.out.println(reverse(s)); // hollo werld
    }


    public static String reverse(String s){
        // Edge cases:
        if( s == null || s == "" || s.length() == 0) throw new IllegalArgumentException("Invalid I/P!");

        char[] ch = s.toCharArray();
        Set<Character> vowels = new HashSet<>(Arrays.asList('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'));

        int l = 0, r = s.length()-1;

        while(l<r){

            while(l<r && !vowels.contains(ch[l])) l++;

            while(l<r && !vowels.contains(ch[r])) r--;

            swap(ch, l, r);
            l++;
            r--;
        }

        return new String(ch);
    }


    public static void swap (char[] ch, int i, int j){
        if (i<j) {
            char temp;
            temp = ch[i];
            ch[i] = ch[j];
            ch[j] = temp;
        }

        return;
    }

}
