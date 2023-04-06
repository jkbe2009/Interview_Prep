
/*
* Click `Run` to execute the snippet below!
*/


import java.io.*;
import java.util.*;


/*
* To execute Java, please define "static void main" on a class
* named Solution.
*
* If you need more classes, simply define them inline.
*/


class Solution {
    public static void main(String[] args) {
        int[][] inp = {
        {1,2,3,4},
        {5,6,7,8},
        {9,10,11,12},
        };

        System.out.println(spiral(inp));   
    }


    public static List<Integer> spiral(int[][] a){
        // O(n*m) || O(1)

        //Validate input:
        if(a == null || a.length == 0 || a[0].length == 0) throw new IllegalArgumentException("Invalid Input!!");

        List<Integer> res = new ArrayList<>();

        int n = a.length, m = a[0].length;
        int top = 0, left = 0, bottom = n-1, right = m-1;
        int count = n*m;

        while(res.size() < count){

            for(int i = left; i <= right && res.size() < count; i++){
                res.add(a[top][i]);
            }
            top++;

            for(int i = top; i <= bottom && res.size() < count; i++){
                res.add(a[i][right]);
            }
            right--;

            for(int i = right; i >= left && res.size() < count; i--){
                res.add(a[bottom][i]);
            }
            bottom--;

            for(int i = bottom; i >= top && res.size() < count; i--){
                res.add(a[i][left]);
            }
            left++;
        }     

        return res;
    }
}


