
import java.util.*;

class reverse_Integer{
    
    public static void main(String[] args) throws Exception {
        int[] inpArr = { 123, 0, -123, 1200, 1234567898, -1234567898};

        for(int inp : inpArr){
            System.out.println(reverse_Int(inp));
        }
    }
    
    /*
    approach 1: 

    Initialize long result with 0
    While num ! = 0
    use standard % to get the last digit 
    Multiply result by 10 and add the last digit
    Reduce the num = num/10
    wend
    return result if not overflowed else return the max or min value accordingly
     */   

     public static int reverse_Int (int num) {
        // O(n) || O(1)

        long res = 0;
        boolean bNeg = false;
        if (num < 0) bNeg = true;

        while (num !=0){
        res = (res*10) + (num%10);
            num/= 10;
        }

        return bNeg ? (res<Integer.MIN_VALUE ? Integer.MIN_VALUE : (int)res) : (res>Integer.MAX_VALUE ? Integer.MAX_VALUE : (int)res) ;
    }

}


