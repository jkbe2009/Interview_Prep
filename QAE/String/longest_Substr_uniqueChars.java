
import java.util.*;

class longest_Substr_uniqueChars{
    
    public static void main(String[] args) throws Exception {
        String[] inpArr = { "abcabc", "abcabcd" , "abcadef", "bbbb", "", null};

        for(String inp : inpArr){
            System.out.println(longest_SubStr_Len_BF(inp));
            System.out.println(longest_SubStr_Len_SW(inp));    
        }
    }
    
    /*
     * approach 1: Brute Force 
     * find all possible substrings and calculate the length of the unique chars only
     * find the maximum of those strings 
     * return the max substring 
     */   

     public static String longest_SubStr_Len_BF(String s){
        // O(n2) || O(1)
        if (s == null || s.length() == 0) return "";

        int len = s.length();
        String res = s.substring(0,1);
        Set<Character> set = new HashSet<>();

        for (int i = 0; i<len-1; i++){
            int j;
            for (j = i; j<len; j++){
                char c = s. charAt(j);
                if (set.contains(c)) break;
                else set.add(c);
            }
            String str = s.substring(i, j);
            if (str.length() > res.length()) res = str;
            set.clear();
        }

        return res;
    }  

    /*
     * approach 2: Sliding window 
     * keep moving the end pointer and mark the character as seen 
     * if a char is already seen start marking the char at start as unseen and keep
     * moving start until the seen for the current char at end is false 
     * now calculate the len between i and j or use a variable to count the length
     * update the max_len if its len > max_len 
     */

     public static String longest_SubStr_Len_SW (String s){
        // O(n) || O(1)
        if (s == null || s.length() == 0) return "";

        int start = 0;
        Set<Character> set = new HashSet<>();
        String res = "";

        for (int end = 0; end<s.length(); end++){
            char c = s.charAt(end);
            while(start < s.length() && !set.add(c)){
                set.remove(s.charAt(start));
                start++;
            }
            if (end-start+1 > res.length()) res = s.substring(start,end+1);
        }

        return res;
    }

}
