
import java.util.*;

class stringReversal_AllTechniques{
    
    public static void main(String[] args) throws Exception {
    String[] inpArr = { "String",
                        "",
                        "I am good!",
                        null,
                        "Machine"};

    System.out.println(reverse1(inpArr[0]));
    System.out.println(reverse1(inpArr[1]));
    System.out.println(reverse2(inpArr[2]));
    System.out.println(reverse3a(inpArr[4]));
    System.out.println(reverse3b(inpArr[4]));
    
    }
    

    public static String reverse1 (String s){
        //O(n) || O(1)

        if (s == null || s.length() == 0) return null;

        int i=0, j=s.length()-1;
        char[] res = s.toCharArray();

        while(i<j){

            char temp  = res[i];
            res[i] = res[j];
            res[j] = temp;
            i++;
            j--;

        }

        return new String(res);
    }
    

    public static String reverse2 (String s){
        //O(n) || O(1)

        if (s == null || s.length() == 0) return null;

        int i=0, j=s.length()-1;
        char[] res = s.toCharArray();

        while(i<j){

            if (res[i] == ' ') {i++; continue;}
            if (res[j]  == ' ') {j--; continue;}

            char temp  = res[i];
            res[i] = res[j];
            res[j] = temp;
            i++;
            j--;

        }

        return new String(res);
    }


    public static String reverse3a (String s){
        //O(n) || O(1)

        if (s == null || s.length() == 0) return null;
        List<Character> vowelList = new ArrayList<> (Arrays.asList('a','e','i','o','u','A','E','I','O','U'));

        int i=0, j=s.length()-1;
        char[] res = s.toCharArray();

        while(i<j){

            //skipping vowels
            if (vowelList.contains(res[i])) {i++; continue;}
            if (vowelList.contains(res[j])) {j--; continue;}

            //swap
            char temp = res[i];
            res[i] = res[j];
            res[j] = temp;
            i++;
            j--;

        }

        return new String(res);
    }


    public static String reverse3b (String s){
        //O(n) || O(1)

        if (s == null || s.length() == 0) return null;
        List<Character> vowelList = new ArrayList<> (Arrays.asList('a','e','i','o','u','A','E','I','O','U'));

        int i=0, j=s.length()-1;
        char[] res = s.toCharArray();

        while(i<j){

            //skipping consonants (non-vowels)
            if (!vowelList.contains(res[i])) {i++; continue;}
            if (!vowelList.contains(res[j])) {j--; continue;}

            //swap
            char temp = res[i];
            res[i] = res[j];
            res[j] = temp;
            i++;
            j--;

        }

        return new String(res);
        }

    }


