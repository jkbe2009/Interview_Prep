
import java.util.*;

class Plus_One{
    
    public static void main(String[] args) throws Exception {
        int[][] inpArr = {
            {1,2,3},
            {7,8,6},
            {3,6,9},
            {3,9,9},
            {9,9,9},
            {},
            null
        };

        for(int[] inp : inpArr){
            System.out.println(Arrays.toString(plus_One_Array(inp)));            
        }

        System.out.println(plus_One_ArrayList(Arrays.asList(1, 2, 3)));
        System.out.println(plus_One_ArrayList(Arrays.asList(7, 8, 6)));
        System.out.println(plus_One_ArrayList(Arrays.asList(3, 6, 9)));
        System.out.println(plus_One_ArrayList(Arrays.asList(3, 9, 9)));
        System.out.println(plus_One_ArrayList(new ArrayList<Integer>(Arrays.asList(3, 9, 9))));
        System.out.println(plus_One_ArrayList(Arrays.asList()));
        System.out.println(plus_One_ArrayList(null));

    }
    
    /*
    approach 1: For arrays

    Loop from n-1 to 0
    if that digit is 9 change the current digit to 0
    else
    add one to that digit and return the array
    End Loop
    create a new array with size n+1
    Put 1 in the first element and return the new array
    */   

    public static int[] plus_One_Array (int[] a) {
        // O(n) || O(1)
        if (a == null || a.length == 0)
            return a;

        for (int i = a.length - 1; i >= 0; i--) {

            if (a[i] < 9) {
                a[i]++;
                return a;
            } else
                a[i] = 0;
        }

        int[] b = new int[a.length + 1];
        b[0] = 1;

        return b;
    }

    /*
    approach 2: For ArrayList

    Loop from n-1 to 0
    if that element is 9 change the current digit to 0
    else
    add one to that element and return the list
    End Loop
    create a new array with size n+1
    Put 1 in the first element and return the same list
    */

    public static List<Integer> plus_One_ArrayList (List<Integer> a) {
        // O(n) || O(1)
        if (a == null || a.size() == 0)
            return a;

        for (int i = a.size() - 1; i >= 0; i--) {

            if (a.get(i) < 9) {
                a.set(i, a.get(i)+1);
                return a;
            } else
                a.set(i, 0);
        }

        // a.add(0,1);

        a.add(0);
        a.set(0, 1);

        return a;
    }

}


