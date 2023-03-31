

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


        int[] nums = new int[] {2,7,11,15};
        int target = 22;
        int [] res = twoSum(nums, target);
        int [] res = twoSum2(nums, target);
        for(int i :res)
            System.out.println(i);


    }


    public static int[] twoSum(int[] nums, int target){
        //int[] res = new int[2];
        Map<Integer, Integer> map = new HashMap<>();


        for(int i = 0; i<nums.length; i++){
            int num = target-nums[i];
            
            if (map.containsKey(num)) return new int[] {map.get(num), i};

            map.put(nums[i], i);
        }

        return new int[]{-1,-1};
    }


    public static int[] twoSum2(int[] nums, int target){
        int l = 0, r= nums.length-1;

        while (l <r){

            int sum = nums[l] + nums[r];
            
            if (sum == target) return new int[] {l, r};
            
            else if (sum < target) l++;
            
            else r--;
        }


        return new int[] {-1, -1};


    }



}
