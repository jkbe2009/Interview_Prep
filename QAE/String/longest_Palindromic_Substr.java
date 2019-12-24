
import java.util.*;

class longest_Palindromic_Substr{
    
    public static void main(String[] args) throws Exception {
        String[] inpArr = {
            "",
            null,
            "b",
            "bb",
            "bbb",
            "abcde",
            "banana"            
        };

        for(String inp : inpArr){
            System.out.println(longest_Pal_Substr_bf(inp));
            System.out.println(longest_Pal_Substr(inp));
        }
    }
    
    /*
    approach 1: brute force

    Generate all possible substrings and check if they are palindrome or not
    If so update the result based on the max length
    return result
    */   

    public static String longest_Pal_Substr_bf (String s) {
        // O(n3) || O(1)
        if (s == null || s.length()==0) return "";

        String res = s.substring(0,1);

        for (int i =0; i<s.length()-1; i++){
            for (int j=i+1; j<s.length(); j++){
                if (isPalindrome (s, i, j) && (j-i+1)> res.length()) {
                     res = s.substring(i,j+1);
                 }
                 //else break;
             }
        }

        return res;
    }

    public static boolean isPalindrome (String s, int i, int j){

        while (i<j){
            if (s.charAt(i) != s.charAt(j)) return false;
            i++; j--;
        }

        return true;
    }


    /*
    approach 2: basic concept of palindrome (reverse of palindromic check)

    for each possible centre positions call the method to return the substr
    start two pointers at the centre and expand until it is a valid palindrome
    return the length of the substr
    update the max(substrings)
    return max
    */ 

    public static String longest_Pal_Substr (String s){
        //O(n2) || O(1)
        if (s == null || s.length()==0) return "";

        String res = s.substring(0,1);

        for (int i=0; i<s.length(); i++){
            
            String s1 = expand(s, i, i);
            if (s1.length() > res.length()) res = s1;
            String s2 = expand(s, i, i+1);
            if (s2.length() > res.length()) res = s2;

        }

        return res;
    }

    public static String expand (String s, int l, int r){

        while ( l>=0 && r<s.length()) {
            if( s.charAt(l) != s.charAt(r)) break;
            l--;
            r++;
        }

        return s.substring(l+1, r);
    }


}


