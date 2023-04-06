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

        Object[][] inp = {
            {100},
            {1000},
            {81000},
            {13},
            {0},
            {-456}
        };

        for (Object[] inpVal : inp)
            System.out.println(smallest((int)inpVal[0]));
    }


    public static int smallest(int inp){
        //Check input:
        if(inp <= 0) throw new IllegalArgumentException("Invalid Input!!!");

        String res = "";

        for (int div = 9; div >=2; div--){
            while(inp % div == 0){
                res = div + res;
                inp = inp / div;
            }
        }

        return (inp == 1) ? Integer.parseInt(res) : -1;
    }

}


