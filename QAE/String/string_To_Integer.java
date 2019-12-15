
import java.util.*;

class string_To_Integer{
    
    public static void main(String[] args) throws Exception {
    String[] inpArr = {"12345", "", null, "-234", "156$32", "+123" };

    for(String inp : inpArr)
        System.out.println(atoi(inp));
    
    }
    
    /*
     * approach: For each character convert it into its numeric equivalent (if valid) else break loop other pair)
     */   

     public static int atoi (String str){
        // O(n) || O(1)

        if (str== null || str.length() == 0) return -1;

        int res=0;
        boolean bNeg = false;
        int i=0;

        if (str.charAt(0) == '-' ) {bNeg = true; i++;}
        else if (str.charAt(0) == '+' ) i++;

        for (; i < str.length(); i++){
        char ch = str.charAt(i);
        if (Character.isDigit(ch)) {
        res = (res *10) + Character.getNumericValue(ch);
        }
        else break;
        }

        return bNeg?-res:res;
        }

}


