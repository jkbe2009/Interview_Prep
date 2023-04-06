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
    {1,2,3,4,5},
    {5,1,2,3,4},
    {4,5,1,2,3},
    {3,4,5,1,2},
    {2,3,4,5,1},
    {-1,-1,-1}
    };

    for (int[] inpVal : inp) System.out.println(findMinEl1(inpVal)); 

    for (int[] inpVal : inp) System.out.println(findMinEl2(inpVal)); 
  }


  public static int findMinEl1(int[] a){
    //Validate Input:
    if(a == null || a.length == 0) throw new IllegalArgumentException("Invalid Input!!!");

    int l = 0, r = a.length-1;
    int m = -1;

    while(l<=r){
      m = (l+r)/2;

      // this is the min element
      if((m==0 || a[m] < a[m-1]) && (m == a.length-1 || a[m] < a[m+1]))
          return m;

      // Go to the unsorted half on the left side
      else if (a[m] < a[r]) r = m-1;

      // Go to the unsorted half on the right side
      else l = m+1;
    }

    return m;
  }


  public static int findMinEl2(int[] a){
    //Validate Input:
    if(a == null || a.length == 0) throw new IllegalArgumentException("Invalid Input!!!");

    int l = 0, r = a.length-1;
    int m = -1;

    while(l<r){
      m = (l+r)/2;
      
      // Go to the unsorted half on the Left side
      if (a[m] < a[r]) r = m;

      // Go to the unsorted half on the right side
      else l = m+1;
    }

    return l;
    }

}


