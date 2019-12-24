
import java.util.*;

class integer_To_String{
    
    public static void main(String[] args) throws Exception {
        int[] inpArr = {123, -123, 0};

        for(int inp : inpArr)
            System.out.println(int_To_String(inp));
        
    }
    
    /*
     * approach: For each digit in the integer add it to a stringbuilder and return the reverse of it with sign (if negative)
     */   

     public static String int_To_String(int num){
        // O(n) || O(1)

        if (num ==0) return "0";
        
        boolean bNeg = false;
        StringBuilder res = new StringBuilder();

        if (num < 0) {bNeg = true; num = -num;}

        while (num >0){
        res = res.append(num%10);
        num = num/10;
        }

        if (bNeg) res.append("-");

        return res.reverse().toString();
    }

}


