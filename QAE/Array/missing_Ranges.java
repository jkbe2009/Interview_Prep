
import java.util.*;

class missing_Ranges{
    
    public static void main(String[] args) throws Exception {
        int[][] inpArr = { 
            null,
            {},
            {0,1,3,50,75},
            {0,1,3,99},
            {4,5,9,36,37,59,98},
            {5,9,78}
         };

        for(int[] inp : inpArr){
            System.out.println(missing_Ranges_Complex (inp, 0, 99));
            System.out.println(missing_Ranges_Simple(inp, 0, 99));
        }
    
    }
    
    /* 
     * approach 1: use the sorted property (complicated version)
     * Loop each element and compare with its next element
     * If the next element is not the subsequent element add the subsequent element into a string
     * If the subsequent element+1 = next element continue
     * else add "->next element-1" to the string and add it to the output list
     * End loop
     * If the last element is not the end of range add "last el+1 -> end of range" to the list
     * return list
     */   

     public static List<String> missing_Ranges_Complex (int[] a, int l, int h) {
        // O(n) || O(n)
        if (a == null || a.length == 0) {
            String s = l +"->"+ h;
            return Arrays.asList(s);
        }

        List<String> result = new ArrayList<> ();
        String s = "";

        if (a[0] != l) {
            s = s + String.valueOf(l);
            if (a[0]-l > 1) s = s + "->" + String.valueOf(a[0]-1);
            result.add(s);
        }

        for (int i=0; i<a.length-1; i++){
            s = "";
            if (a[i+1]-a[i] == 2) {
                s = s + String.valueOf(a[i]+1);	
                result.add(s);	
            }
            else if (a[i+1]-a[i] > 2) {
                s = String.valueOf(a[i]+1) +"->"+ String.valueOf(a[i+1]-1);
                result.add(s);
            }
        }

        s = "";
        if (a[a.length-1] != h) {
            s = s + String.valueOf(a[a.length-1]+1);
            if (h-a[a.length - 1] > 1) s = s +"->" + String.valueOf(h);
            result.add(s);
        }

        return result;
        }


    /*
     * approach 2: use the sorted property (simple modularised version) 
     * Add artificial elements at the beginning and end to solve it easily
     * initialise prev = l-1 
     * Loop through every element until last element +1 
     * if the diff b/w curr and prev is >=2 call a method to form a string 
     * add that string to the result 
     * prev = curr 
     * End Loop 
     */
    
     public static List<String> missing_Ranges_Simple (int[] a, int l, int h){
        // O(n) || O(n)
        if (a == null || a.length == 0) {
            String s = l +"->"+ h;
            return Arrays.asList(s);
        }

        int prev = l-1, curr;
        List<String> res = new ArrayList<>();

        for (int i=0; i<=a.length; i++) {
            curr = (i == a.length) ? h+1 : a[i];
            if (curr - prev >= 2) res.add(getRange(prev+1,curr-1));
            prev = curr;
        }
    
        return res;
    }

     public static String getRange (int from, int to) {
        return (from == to) ? String.valueOf(from) : from +"->"+ to ;
    }

    }


