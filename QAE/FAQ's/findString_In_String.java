
import java.util.*;

class findString_In_String{
    
    public static void main(String[] args) throws Exception {
    String[][] inpArr = {   {"","art"},
                            {"karthik", ""},
                            {null, "art"},
                            {"karthik", null},
                            {"karthik", "art"},
                            { "karthik", "fdaf" },
                            {"karthik", "thi"},
                            { "karthik", "thic" },
                        };

    for(String inp[] : inpArr)
        System.out.println(strstr(inp[0],inp[1]));
    }
    

    public static int strstr(String hay, String needle) {
        // O(nm) | O(1)

        if (needle == null || needle.length() == 0 || hay == null || hay.length() == 0)
            return -1;
        int n = needle.length(), m = hay.length();

        for (int i = 0; i < m - n; i++) {
            int j = 0;

            while (j < n && needle.charAt(j) == hay.charAt(i + j))
                j++;

            if (j == n)
                return i;
        }

        return -1;
    }

}


