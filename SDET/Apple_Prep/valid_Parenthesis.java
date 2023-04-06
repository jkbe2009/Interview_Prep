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
        String[][] inp = {
            {"{}[]()"},
            {"[{()}]"},
            {"[{(]})"},
            {"[{"},
            {"]}"},
            {""}
        };

        for (String[] str : inp) System.out.println(isValid(str[0]));
    }


    public static boolean isValid(String s){
        //Validate Input:
        if( s == null || s.length() == 0) throw new IllegalArgumentException("Invalid Input!!!");

        //if length is odd i.e not balanced
        if(s.length()%2 !=0) return false;

        Stack<Character> st = new Stack<>();

        Map<Character, Character> map = new HashMap<>();
        map.put('(', ')');
        map.put('{', '}');
        map.put('[', ']');

        for (char ch : s.toCharArray()){
            //if its a open paranthesis:
            if(map.containsKey(ch)) st.push(ch);

            //close paranthesis:
            else{
                if(st.isEmpty()) return false;

                if(map.get(st.pop()) != ch) return false;
            }
        }

        return st.isEmpty();
    }
}
