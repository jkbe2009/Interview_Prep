
import java.util.*;

class validPalindrome_String {

    public static void main(String[] args) throws Exception {
        String inp1 = null;
        String inp2 = "";
        String inp3 = "ma dam";
        String inp4 = "1$212!1";
        String inp5 = "Ma12 d21tam";
        String inp6 = "";

        System.out.println(isValidPalindromeStr(inp3));
    }

    public static boolean isValidPalindromeStr(String s) {
        // O(n) || O(1)
        if (s == null || s.length() == 0)
            throw new IllegalArgumentException("Invalid Input!");

        int l = 0, r = s.length() - 1;
        // “Ma12 d21am”

        while (l < r) {
            while (l < r && !Character.isLetterOrDigit(s.charAt(l)))
                l++;
            while (l < r && !Character.isLetterOrDigit(s.charAt(r)))
                r--;

            if (Character.toUpperCase(s.charAt(l)) != Character.toUpperCase(s.charAt(r)))
                return false;

            l++;
            r--;
        }

        return true;
    }

}
