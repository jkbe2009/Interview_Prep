
import java.util.*;

class len_longest_Substr_uniqueChars{
    
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
     * find the maximum length of those strings 
     * return the max_len
     * 
     */   

     public static int longest_SubStr_Len_BF(String s){
        // O(n2) || O(1)
        if (s == null || s.length() == 0) return -1;

        int len = s.length();
        int max_len = 0;

        for (int i = 0; i<len-1; i++){
            boolean[] seen = new boolean[256];
            int length = 0;
            for (int j = i; j<len; j++){
                char c = s. charAt(j);
                if (seen[c] == true) break;
                length++;
                seen[c] = true;
            }
        if (length > max_len) max_len = length;
        }

        return max_len;
    }   

    /*
     * approach 2: Sliding window 
     * keep moving the end pointer and mark the character as seen 
     * if a char is already seen start marking the char at start as unseen and keep
     * moving start until the seen for the current char at end is false 
     * now calculate the len between i and j or use a variable to count the length
     * update the max_len if its len > max_len 
     */

     public static int longest_SubStr_Len_SW (String s){
        // O(n) || O(1)
        if (s == null || s.length() == 0) return -1;

        int start = 0;
        int len=0, max_len=0;
        boolean[] seen = new boolean[256];

        for (int end = 0; end<s.length(); end++){
            char c = s.charAt(end);
            while (start<s.length() && seen[c] == true){
                seen[s.charAt(start)] = false;
                start++;
                len--;
            }
            seen[c] = true;
            len++;
            
            max_len = Math.max (len, max_len);
        }

        return max_len;
    }

}
