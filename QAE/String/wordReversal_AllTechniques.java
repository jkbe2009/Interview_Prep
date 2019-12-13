
import java.util.*;

class wordReversal_AllTechniques{
    
    public static void main(String[] args) throws Exception {
    String inpArr1 = "the sky is blue";
    String inpArr2 = " the sky  is   blue  ";

    System.out.println(reverse1(inpArr1));
    System.out.println(reverse2(inpArr2));
    System.out.println(reverse3(inpArr1));
    
    }


    public static String reverse1 (String s){
        // O(n) || O(m)

        String[] strArr  = s.split(" ");
        StringBuilder sb = new StringBuilder();

        for(int i=strArr.length-1; i>=0; i--){
            sb = sb.append(strArr[i]);
            if (i != 0) sb = sb.append(" ");
        }

        return sb.toString();
    }


    public static String reverse2 (String s){
        // O(n) || O(1)

        if (s == null || s.length() == 0) return null;

        int beg=0, end=0;
        boolean bFlag = false;
        StringBuilder sb = new StringBuilder();

        for(int i= s.length()-1; i>=0; i--){

            if (!bFlag && s.charAt(i) != ' ') { end = i; bFlag = true;}

            if (bFlag && s.charAt(i) != ' ' && s.charAt(i-1) == ' ' ) {
                beg = i;
                sb.append(s.substring(beg,end+1)).append(" ");
                bFlag = false;
            }
        }
    
        return sb.toString().trim();
    }


    public static String reverse3 (String s){
        // O(n) || O(1)

        if (s == null || s.length() == 0) return null;

        int beg = 0;
        char[] res = s.toCharArray();
        int len = res.length;

        for(int i=0; i<len; i++){
            if (i == len-1 || res[i+1] == ' ')
            {
                reversal(res,beg,i);
                beg = i+2;
            }
        }

        reversal(res,0,len-1);
        return new String(res);
        }


    public static void reversal(char[] ch, int i, int j) {
        while(i<j){
            char temp = ch[i];
            ch[i] = ch[j];
            ch[j] = temp;
            i++;
            j--;
        }
        return;
    }

}


