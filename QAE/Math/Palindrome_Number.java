
import java.util.*;

class Palindrome_Number{
    
    public static void main(String[] args) throws Exception {
        int[] inpArr = {121, 1234321, -121, 12210 };

        for(int inp : inpArr){
            System.out.println(is_Palindrome_To_String(inp));
            System.out.println(is_Palindrome_Reversal(inp));
            System.out.println(is_Palindrome_Digits(inp));
        }
    }
    
    /*
    approach 1: brute force

    Check for edge cases
    if num is negative or the last digit is zero return false
    convert the num to string
    use two pointers i and j at the start and end respectively
    while i<j
    if the chars at i and j don't match return false
    i++, j--
    wend
    return true
    */   

    public static boolean is_Palindrome_To_String(int num) {
        // O(n) || O(n)
        if (num < 0 || (num != 0 && num % 10 == 0))
            return false;
        String s = String.valueOf(num);
        int i = 0, j = s.length() - 1;

        while (i < j) {

            if (s.charAt(i) != s.charAt(j))
                return false;
            i++;
            j--;
        }

        return true;
    }

    /*
    approach 2 : compare with reversed number

    reverse num (use long)
    compare reversed num with num
    return comparison result
    */

    public static boolean is_Palindrome_Reversal(int num) {
        // O(n) || O(n)
        if (num < 0 || (num != 0 && num % 10 == 0))
            return false;

        int revNum = reverse(num);
        return num == (int) revNum;
    }

    public static int reverse (int num) {
        int res = 0;

        while (num>0){
        res = res*10 + num%10;
        num /= 10;
        }
        return res;
    }

    /*
    approach 3: number manipulation

    find the factor (number of zero’s)
    while the number is > 0
    get the last digit using num%10
    get the first digit using num/factor
    compare both the digits and return false if not same
    remove both the digits from the number by doing (num%factor)/10
    factor = factor/100 (to account for the lost two digits)
    wend
    */

    public static boolean is_Palindrome_Digits(int num) {
        // O(n) || O(n)
        if (num < 0 || (num != 0 && num % 10 == 0))
            return false;

        int temp = num;
        int factor = 1;

        while (num >= 10) {
            factor = factor * 10;
            num = num / 10;
        }

        num = temp;

        while (num > 0) {
            int last = num % 10;
            int first = num / factor;
            if (first != last)
                return false;
            num = (num % factor) / 10;
            factor = factor / 100;
        }

        return true;
    }

}


