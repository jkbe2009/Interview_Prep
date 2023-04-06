
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
            {13,14,15,16}
        };

        for(int i = 0; i < inp.length; i ++){
            for(int j = 0; j < inp[i].length; j++){
                System.out.print(inp[i][j]  + "   ");
            }
            System.out.println("");
        }

        System.out.println("");

        //inp = rotate_BF(inp);

        rotate(inp);

        for(int i = 0; i < inp.length; i ++){
            for(int j = 0; j < inp[i].length; j++){
                System.out.print(inp[i][j]  + "   ");
            }
            System.out.println("");
        }
    }


    public static int[][] rotate_BF(int[][] inp){
        //Valid input:
        if(inp == null || inp.length == 0) throw new IllegalArgumentException("Invalid Input!!");


        int[][] res = new int[inp.length][inp[0].length];
        int len = inp.length-1;


        for(int i = 0; i < inp.length; i++){
            for(int j = 0; j < inp[i].length; j++){
                res[j][len-i] = inp[i][j];
            }
        }

        return res;
    }


    public static void rotate(int[][] inp){
        //Validate input:
        if(inp == null || inp.length == 0) throw new IllegalArgumentException("Invalid Input!!");

        //Transpose Matrix in place
        for (int i = 0; i < inp.length; i++){
            for(int j = i+1; j < inp[i].length; j++){
                int temp = inp[i][j];
                inp[i][j] = inp[j][i];
                inp[j][i] = temp;
            }
        }

        //Swap columns in place
        int i = 0, j = inp[0].length-1;

        while(i<j){
            //swap values
            for(int k =0; k < inp.length; k++){
            int temp = inp[k][i];
            inp[k][i] = inp[k][j];
            inp[k][j] = temp;
            }
            i++;
            j--;
        }
    }


}


