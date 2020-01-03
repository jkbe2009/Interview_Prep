
import java.util.*;

class Single_Number{
    
    public static void main(String[] args) throws Exception {
        int[][] inpArr = {
            { 1, 1, 2, 2, 3, 3, 5, 5, 7},
            { 1, 3, 1, 5, 2, 3, 2, 5, 7 },
            {},
            null
        };

        for(int[] inp : inpArr){
            System.out.println(single_Number(inp));
            System.out.println(single_Number_XOR(inp));
        }
    }
    
    /*
    approach 1: HashSet

    create a HashSet of Integer
    loop through the array input and and the elements one by one
    if the Set does not contain the element (Seeing for the first time) continue
    else remove the element from the set
    end loop
    check if set contains only one element and return the first element
    else return -1    
    */   

    public static int single_Number(int[] a) {
        // O(n) || O(n)
        if (a == null || a.length == 0)
            return -1;

        HashSet<Integer> set = new HashSet<>();

        for (int i = 0; i < a.length; i++) {
            int el = a[i];
            if (set.contains(el))
                set.remove(el);
            else
                set.add(el);
        }

        return set.size() == 0 ? -1 : set.iterator().next();
    }

    /*
    approach 2 : XOR operator

    XOR is both commutative and associative
    XOR of all the numbers one by one will cancel each other out (numbers which occurs even times) 
    except the odd one which occurs only once
    store the XOR of all numbers in a result variable
    return result if its not zero else return -1    
    */   

    public static int single_Number_XOR(int[] a) {
        // O(n) || O(1)
        if (a == null || a.length == 0)
            return -1;

        int result = 0;

        for (int i : a)
            result = result ^ i;

        return result == 0 ? -1 : result;
    }

}


